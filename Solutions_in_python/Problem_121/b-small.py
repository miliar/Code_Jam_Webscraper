#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright © 2009-2013 by T. Chan.

from __future__ import division,with_statement#,absolute_import,print_function
import __builtin__ as builtin,sys,os,os.path,re,time,hashlib,base64,StringIO as io,cPickle as pickle
import operator,array,itertools,bisect,collections,heapq
import pprint,pdb,traceback,warnings
from pdb import set_trace as debug
from math import hypot,pi,sin,cos,tan,sqrt,floor,ceil,asin,fsum
from itertools import islice,izip,imap
from collections import namedtuple,deque

# All the imports needed for liblib
import ctypes,subprocess,base64,hashlib,tempfile
class liblib(object):
	GCC_SHARED = {'darwin':'-dynamiclib','linux2':'-shared'}[sys.platform]
	GCC_WARN = ('-Wall','-Wformat=2','-Winit-self','-Wuninitialized','-Wmissing-include-dirs',
		'-Wswitch-default','-Wswitch-enum','-Wstrict-aliasing=2',
		'-Wextra','-Wno-missing-field-initializers','-Wundef','-Wshadow','-Wpointer-arith',
		'-Wbad-function-cast','-Wcast-qual','-Wcast-align','-Wwrite-strings',
		'-Wsign-compare','-Wstrict-prototypes','-Wold-style-definition',
		'-Wno-long-long','-Wdisabled-optimization')
	# -Wshorten-64-to-32 replaced with -Wconversion in GCC 4.3. Sigh. Also -Wsign-conversion.
	GCC_WARN_MAYBE = ('-Wunreachable-code','-Wpacked','-Wpadded','-Wmissing-noreturn',
		'-Wmissing-format-attribute','-pedantic','-Wcomment')
	GCC_C_WARN = GCC_WARN + GCC_WARN_MAYBE + ('-Wnested-externs',)
	GCC_CC_WARN = ('-Wabi','-Wctor-dtor-privacy','-Weffc++','-Wstrict-null-sentinel','-Wold-style-cast',
		'-Woverloaded-virtual','-Wsign-promo',)
	GCC_ObjC_WARN = ('-Wselector','-Wstrict-selector-match','-Wundeclared-selector')
	GCC_C = ('gcc','-Os','-pipe',GCC_SHARED,'-x','c','-std=gnu99') + GCC_C_WARN
	NONCE = os.urandom(128)
	@staticmethod
	def hh(h,l):
		ret = h()
		for x in l:
			ret.update(x)
		ret.update(ret.digest())
		return ret.digest()
	@classmethod
	def lib(self,code,cmdline=GCC_C):
		s = base64.b32encode(self.hh(hashlib.sha256,(os.urandom(32),self.NONCE,code,self.NONCE))).strip('=')
		fd,path = tempfile.mkstemp(prefix='templib.%s.'%s)
		try:
			os.close(fd)
			args = tuple(cmdline)+('-o',os.path.join(os.path.curdir,path),'-')
			p = subprocess.Popen(args,stdin=subprocess.PIPE)
			p.communicate(code)
			if p.returncode:
				raise subprocess.CalledProcessError(returncode=p.returncode,cmd=args)
			lib = ctypes.cdll.LoadLibrary(path)
			return lib
		finally:
			os.unlink(path)
	@classmethod
	def extern_c(self,f):
		fn,argtypes,restype,code = f()
		f = self.lib(code)[fn]
		f.argtypes = argtypes
		f.restype = restype
		return f

	def __init__(self):
		self.d = {}
	def add(self,code):
		d = self.d
		lib = d.get(code)
		if lib is None:
			lib = self.lib(code)
			d[code] = lib
		return lib
	def __getitem__(self,i):
		return self.d[i]

@liblib.extern_c
def process2c():
	ui = ctypes.c_uint
	return ('process2c',(ui,ui,ui, ui,ui,ui,ui,ui,ui,ui,ui,ui,ui),ui,"""
typedef unsigned int ui;

ui process2c(ui E, ui R, ui N, ui v0, ui v1, ui v2, ui v3, ui v4, ui v5, ui v6, ui v7, ui v8, ui v9, ui v10) {
	ui v[] = {v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10};
	ui best = 0;
	ui limit = 1;
	for (ui i=0; i<N; i++) { limit *= E+1; }
	for (ui xx=0;xx<limit;xx++) {
		ui x=xx;
		ui e=E;
		ui gain=0;
		for (ui i=0;i<N;i++) {
			ui spend = x%(E+1);
			x/=(E+1);
			if (!(spend <= e && e <= E)) { goto fail; }
			gain += spend*v[i];
			e += R-spend;
		}
		if (gain>best){ best=gain; }
fail:
		(void)0;
	}
	return best;
}
""")

def process2(E,R,vs):
	if R>=E: return sum(vs)*E
	return process2c(E,R,len(vs),*(vs+[0]*10)[:10])
	maxgain = 0
	Ep1 = E+1
	for x in xrange(Ep1**len(vs)):
		e = E
		gain=0
		for v in vs:
			spend,x = x%Ep1,x//Ep1
			if not (spend <= e <= E): break
			gain += spend*v
			e += R-spend
		else:
			maxgain = max(maxgain,gain)
	return maxgain

def process(f_, out):
	T_, = map(int,f_.readline().strip().split())
	for X_ in range(1,T_+1):
		E,R,N = map(int,f_.readline().strip().split())
		vs = map(int,f_.readline().strip().split())
		assert len(vs) == N

		output = process2(E,R,vs)
		
		out.write('Case #%d: %s\n' % (X_,output))
		out.flush()

TEST_DATA=(r''' 3
5 2 2
2 1
5 2 2
1 2
3 3 4
4 1 3 5
Case #1: 12
Case #2: 12
Case #3: 39
 ''',)#r'''  ''')

# Running
def pmfunc(func):
	def wrapped_func(*args,**kwargs):
		try: return func(*args,**kwargs)
		except: traceback.print_exc(); pdb.post_mortem(); raise
	return wrapped_func
if __debug__: process=pmfunc(process)

def process_test(d):
	f_,out = io.StringIO(d),io.StringIO()
	process(f_,out)
	return out.getvalue()

def process_file(fn,auto=False):
	for ext in ('.in', '.in.txt', ''):
		if fn.endswith(ext): base = fn[:-len(ext)] if ext else fn; break
	i = 0
	while 1:
		path = '%s.out%d.txt'%(base,i); path2 = 'broken-'+path
		p1,p2 = os.path.exists(path), os.path.exists(path2)
		if not (p1 or p2): break
		if auto and p1: print "! %s exists"%(path if p1 else path2); return
		i += 1
	print ">> %s"%path
	success = None
	try:
		with open(fn,'rb') as f_,open(path,'wb') as out: process(f_,out)
		success = True
	finally:
		if not success: os.rename(path,path2)
	return success

def main():
	def ts(prefix='>',delta=True,old=[None]):
		t = time.time()
		diff, old[0] = (delta and (old[0] is not None)) and ' d%.6f'%(t - old[0]) or '', t
		print '%s %s %.6f%s'%(prefix,time.strftime('%F %T %z',time.gmtime(t)),t,diff)

	ts(' ',delta=False)

	qid = rundir = testcache = None
	mydir,myfile = os.path.split(os.path.join(os.path.curdir,__file__))
	assert os.path.abspath(mydir) == os.path.abspath(os.path.curdir)
	if myfile.endswith('.py'):
		qid,rundir,t,myhash = myfile[:-3].upper(), os.path.join(mydir,'runs'), time.time(), hashlib.sha256()
		if not os.path.isdir(rundir): os.makedirs(rundir)
		runfile = os.path.join(rundir, '%s_%s.%06dz.py'%(qid,time.strftime('%F-%H%M%S',time.gmtime(t)),round(t%1*1e6)))
		assert not os.path.exists(runfile)
		with open(__file__,'rb') as fin, open(runfile,'wb') as fout:
			d = fin.readline()+fin.readline(); fout.write(d); myhash.update(d)
			fout.write('\n# RUN at %s %.6f\n# cmdline = %r\n\n'%(time.strftime('%F %T %z',time.gmtime(t)),t,sys.argv))
			d = fin.read(); fout.write(d); myhash.update(d)
		testcache = os.path.join(rundir,'%s_%s.passed'%(qid,base64.b32encode(myhash.digest()).rstrip('=')))
		del fin, fout, t, runfile, myhash

	if 'gen' in globals(): gen(os.path.join(mydir,myfile+'.pickle'), ts)
	l = sys.argv[1:]
	auto=False
	if not l:
		if not (testcache and os.path.exists(testcache)):
			def td(d):
				if isinstance(d,str): d=d.split('Case #1:',1); return d[0].strip(), 'Case #1:' + d[1].rstrip() + '\n'
				return d
			for test_data in TEST_DATA:
				if not test_data.strip(): print >>sys.stderr, '! Empty test case.'; return
				test_input,expected_output=td(test_data)
				my_output = process_test(test_input)
				if my_output != expected_output: print >>sys.stderr, "!!! Wrong output."; print >>sys.stderr, my_output; return
				ts('v')
			if testcache: open(testcache,'wb').close()
		if qid:
			expr = re.compile(r'\A%s\-(?:large|small-attempt[0-9]|(?:large|small)\-practice)\.in(?:\.txt)?\Z'%qid)
			auto=True
			l = list(f for f in os.listdir(mydir) if expr.match(f))
	for x in l:
		ts('.',delta=False)
		print '<< %s'%x
		if x == '-': process(sys.stdin,sys.stdout)
		else: process_file(x,auto=auto)
		ts('>')

if __name__ == '__main__':
	main()
