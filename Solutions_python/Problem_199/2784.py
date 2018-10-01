{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# imports\n",
    "import numpy as np # http://www.numpy.org/\n",
    "import math # https://docs.python.org/2/library/math.html\n",
    "import itertools as it # https://docs.python.org/2/library/itertools.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "basepath = '/home/epg/halde/codejam/2017/Quals/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "testset = 'A-large'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def do_flip(S, K, i):\n",
    "    return S[:i] + S[i:i+K].replace('-', '.').replace('+', '-').replace('.', '+') + S[i+K:]\n",
    "\n",
    "def do_solve(S, K):\n",
    "    #print S, K\n",
    "    \n",
    "    if S.find('-') == -1:\n",
    "        return 0\n",
    "    \n",
    "    if len(S)-K < 3:\n",
    "        s = len(S) - K\n",
    "        e = s + K - (len(S) - K)\n",
    "        if S.find('-', s, e) != -1 and S.find('+', s, e) != -1:\n",
    "            return 'IMPOSSIBLE'\n",
    "    \n",
    "    n = 0\n",
    "    i = 0\n",
    "    c = '+'\n",
    "    while i < len(S)-K+1:\n",
    "        while i < len(S)-K+1 and S[i] == c:\n",
    "            i += 1\n",
    "        \n",
    "        if i == len(S)-K+1:\n",
    "            break\n",
    "        \n",
    "        #print S, i, c\n",
    "        \n",
    "        S = do_flip(S, K, i)\n",
    "        c = S[i]\n",
    "        \n",
    "        i += 1\n",
    "        n += 1\n",
    "    \n",
    "    #print S, i, c\n",
    "    \n",
    "    if S.find('-') != -1:\n",
    "        return 'IMPOSSIBLE'\n",
    "    \n",
    "    return n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 3\n",
      "Case #2: 0\n",
      "Case #3: IMPOSSIBLE\n",
      "Case #4: IMPOSSIBLE\n",
      "Case #5: 2\n",
      "Case #6: 1\n",
      "Case #7: IMPOSSIBLE\n",
      "Case #8: 0\n",
      "Case #9: IMPOSSIBLE\n",
      "Case #10: IMPOSSIBLE\n",
      "Case #11: 0\n",
      "Case #12: 3\n",
      "Case #13: IMPOSSIBLE\n",
      "Case #14: IMPOSSIBLE\n",
      "Case #15: IMPOSSIBLE\n",
      "Case #16: 3\n",
      "Case #17: 1\n",
      "Case #18: IMPOSSIBLE\n",
      "Case #19: IMPOSSIBLE\n",
      "Case #20: 9\n",
      "Case #21: 8\n",
      "Case #22: IMPOSSIBLE\n",
      "Case #23: IMPOSSIBLE\n",
      "Case #24: IMPOSSIBLE\n",
      "Case #25: IMPOSSIBLE\n",
      "Case #26: 2\n",
      "Case #27: 1\n",
      "Case #28: 2\n",
      "Case #29: 2\n",
      "Case #30: IMPOSSIBLE\n",
      "Case #31: IMPOSSIBLE\n",
      "Case #32: IMPOSSIBLE\n",
      "Case #33: IMPOSSIBLE\n",
      "Case #34: 2\n",
      "Case #35: IMPOSSIBLE\n",
      "Case #36: IMPOSSIBLE\n",
      "Case #37: IMPOSSIBLE\n",
      "Case #38: 3\n",
      "Case #39: IMPOSSIBLE\n",
      "Case #40: IMPOSSIBLE\n",
      "Case #41: IMPOSSIBLE\n",
      "Case #42: IMPOSSIBLE\n",
      "Case #43: 4\n",
      "Case #44: IMPOSSIBLE\n",
      "Case #45: 1\n",
      "Case #46: 1\n",
      "Case #47: 3\n",
      "Case #48: IMPOSSIBLE\n",
      "Case #49: 1\n",
      "Case #50: 2\n",
      "Case #51: IMPOSSIBLE\n",
      "Case #52: IMPOSSIBLE\n",
      "Case #53: IMPOSSIBLE\n",
      "Case #54: 1\n",
      "Case #55: 1\n",
      "Case #56: IMPOSSIBLE\n",
      "Case #57: 1\n",
      "Case #58: 0\n",
      "Case #59: IMPOSSIBLE\n",
      "Case #60: IMPOSSIBLE\n",
      "Case #61: IMPOSSIBLE\n",
      "Case #62: 1\n",
      "Case #63: IMPOSSIBLE\n",
      "Case #64: IMPOSSIBLE\n",
      "Case #65: 1\n",
      "Case #66: IMPOSSIBLE\n",
      "Case #67: 2\n",
      "Case #68: IMPOSSIBLE\n",
      "Case #69: 1\n",
      "Case #70: 2\n",
      "Case #71: 2\n",
      "Case #72: IMPOSSIBLE\n",
      "Case #73: 5\n",
      "Case #74: IMPOSSIBLE\n",
      "Case #75: IMPOSSIBLE\n",
      "Case #76: IMPOSSIBLE\n",
      "Case #77: 0\n",
      "Case #78: 3\n",
      "Case #79: IMPOSSIBLE\n",
      "Case #80: IMPOSSIBLE\n",
      "Case #81: 1\n",
      "Case #82: 2\n",
      "Case #83: IMPOSSIBLE\n",
      "Case #84: 2\n",
      "Case #85: 3\n",
      "Case #86: 0\n",
      "Case #87: 2\n",
      "Case #88: IMPOSSIBLE\n",
      "Case #89: 2\n",
      "Case #90: 0\n",
      "Case #91: IMPOSSIBLE\n",
      "Case #92: IMPOSSIBLE\n",
      "Case #93: 1\n",
      "Case #94: 0\n",
      "Case #95: 1\n",
      "Case #96: IMPOSSIBLE\n",
      "Case #97: IMPOSSIBLE\n",
      "Case #98: IMPOSSIBLE\n",
      "Case #99: IMPOSSIBLE\n",
      "Case #100: IMPOSSIBLE\n"
     ]
    }
   ],
   "source": [
    "with open(basepath + testset + '.in') as fin, open(basepath + testset + '.out', 'w') as fout:\n",
    "    T = int(fin.readline().rstrip('\\r\\n'))\n",
    "    for i in xrange(T):\n",
    "        S, K = tuple(fin.readline().rstrip('\\r\\n').split(' '))\n",
    "        K = int(K)\n",
    "        \n",
    "        sol = do_solve(S, K)\n",
    "        \n",
    "        sol_string = 'Case #{}: {}'.format(i+1, sol)\n",
    "        fout.write(sol_string + '\\n')\n",
    "        print sol_string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python2",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
