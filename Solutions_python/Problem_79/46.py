#!/usr/bin/env python

_FMT_ = 'Case #%d: %s\n'
f = open('in','r')
_T_ = int(f.readline())

import sys
import re
if len(sys.argv) > 1:
	_jobs_ = _T_/4
	_jid_ = int(sys.argv[1])
	_t0_ = _jobs_ * _jid_
	_t1_ = _jobs_ *(_jid_+1)
	if _jid_ == 3: _t1_ = _T_
	g = open('out'+str(_jid_),'w')
else:
	_jid_ = -1
	_t0_ = 0
	_t1_ = _T_
	g = open('out','w')

for _t_ in xrange(_T_): 

	#INPUT
	N, M  = (int(x) for x in f.readline().strip().split())
	words = []
	for n in xrange(N):
		words.append(f.readline().strip())
	g.write('Case #%d:' %(_t_+1,))
	for m in xrange(M):
		seq = f.readline().strip()
		
		max_score = 0
		max_word = words[0]
		for word in words:
			score = 0
			left = [w for w in words if len(w)== len(word)]
			c = -1
			while len(left) > 1:
				c += 1
				ch = seq[c]
				for w in left:
					if ch in w: break
				else: continue  # skip to the next one

				to_remove = []
				if ch not in word: 
					score += 1
					for w in left: 
						if ch in w: to_remove.append(w)
					for w in to_remove: left.remove(w)
				else:
					for j in xrange(len(word)):
						if word[j] == ch: 
							to_remove = []
							for w in left: 
								if w[j] !=ch: to_remove.append(w)
							for w in to_remove: left.remove(w)
						else:
							to_remove = []
							for w in left:
								if w[j] ==ch: to_remove.append(w)
							for w in to_remove: left.remove(w)

			if score > max_score:
				max_word = word
				max_score = score
		g.write(' %s' %(max_word,))
	g.write('\n')

if _jid_ >= 0: print 'Job %d finished *********************' %(_jid_)

