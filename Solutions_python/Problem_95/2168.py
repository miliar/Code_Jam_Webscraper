import string
inp = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
bla = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
translatelist = [['z','q'],['q','z']]

def trans(c,dir=[0,1]):
	isupper = False
	if c in string.lowercase:
		isupper = True
	c = string.lower(c)
	for i in translatelist:
		if i[dir[0]] == c:
			if isupper:
				return i[dir[1]]
			else:
				return string.upper(i[dir[1]])

	return "-"

for i in xrange(0, len(inp)):
	translatelist.append([inp[i], bla[i]])

# for i in string.lowercase:
# 	 print "%s-%s" % (i, trans(i,[1,0]) )
transl = []
transl.append('ejp mysljylc kd kxveddknmc re jsicpdrysi')
transl.append('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
transl.append('de kr kd eoya kw aej tysr re ujdr lkgc jv')
transl.append('hello i am the google code jam test data')
transl.append('how are you')
transl.append('aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee')
transl.append('y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd')
transl.append('schr rkxc tesr aej dksl tkrb xc')
transl.append('ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi')
transl.append('ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi')
transl.append('ejp feic uyx kd mkoc rbc varbylepcys rbcepcx')
transl.append('rbcpc kd se ysdtcp')
transl.append('aej tysr dcmm rbksld yr xc neksl qeeex')
transl.append('bet ypc aej bemiksl jv ncfyjdc kx y veryre')
transl.append('tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd')
transl.append('eb seeeee lellymep kd bcyici wep rbc epvbysylc')
transl.append('eb xa lei mcrd xyoc ejr')
transl.append('na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd')
transl.append('eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq')
transl.append('njww rpasiyxcpc ysi yxjxj')
transl.append('aej oset aej tysr re')
transl.append('vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd')
transl.append('mcr mkvd ie tbyr bysid ie')
transl.append('eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr')
transl.append('rpysdmyrksl rchr kd ser leped drpcslrb')
transl.append('drpcslrb kd leped drpcslrb')
transl.append('rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx')
transl.append('lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd')
transl.append('kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd')
transl.append('pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb')
for j in xrange(0,len(transl)):

	outp = "Case #%d: " % (int(j)+1)
	for i in xrange(0, len(transl[j])):
		outp += trans(transl[j][i],[1,0])
	print outp
