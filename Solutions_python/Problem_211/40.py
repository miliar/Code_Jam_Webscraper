{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(Ns,U):\n",
    "    #print Ns, U\n",
    "    if U == 0:\n",
    "        mult = 1\n",
    "        for x in Ns:\n",
    "            mult *= x\n",
    "        return mult\n",
    "    \n",
    "    equal = 1\n",
    "    for i in range(1,len(Ns)):\n",
    "        if Ns[0] == Ns[i]:\n",
    "            equal += 1\n",
    "       \n",
    "    inc = U/equal\n",
    "    \n",
    "    if equal != len(Ns):\n",
    "        inc = min(inc, Ns[equal] - Ns[0])\n",
    "            \n",
    "    for i in range(equal):\n",
    "        Ns[i] += inc\n",
    "     \n",
    "    #print \"inc\", inc, equal\n",
    "    return solve(Ns, U-inc*equal)"
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def parse(text):\n",
    "    T = int(text.next())\n",
    "    for i in range(T):\n",
    "        N,K = [int(x) for x in text.next().rstrip().split(\" \")]\n",
    "        U = float(text.next())\n",
    "        Ns = [float(x) for x in text.next().rstrip().split(\" \")]\n",
    "        \n",
    "        Ns = sorted(Ns)\n",
    "        soln = solve(Ns,U)\n",
    "        \n",
    "        print \"Case #%d: %f\" % (i+1, soln)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "TEXT = \"\"\"4\n",
    "4 4\n",
    "1.4000\n",
    "0.5000 0.7000 0.8000 0.6000\n",
    "2 2\n",
    "1.0000\n",
    "0.0000 0.0000\n",
    "2 1\n",
    "0.0000\n",
    "0.9000 0.8000\n",
    "2 1\n",
    "0.1000\n",
    "0.4000 0.5000\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1.000000\n",
      "Case #2: 0.250000\n",
      "Case #3: 0.720000\n",
      "Case #4: 0.250000\n"
     ]
    }
   ],
   "source": [
    "parse(x for x in TEXT.splitlines())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1.000000\n",
      "Case #2: 0.250000\n",
      "Case #3: 0.720000\n",
      "Case #4: 0.250000\n",
      "Case #5: 0.000606\n",
      "Case #6: 0.068064\n",
      "Case #7: 0.000000\n",
      "Case #8: 0.027772\n",
      "Case #9: 0.003095\n",
      "Case #10: 0.010747\n",
      "Case #11: 0.444422\n",
      "Case #12: 0.002488\n",
      "Case #13: 0.999900\n",
      "Case #14: 1.000000\n",
      "Case #15: 0.026152\n",
      "Case #16: 0.001009\n",
      "Case #17: 0.004564\n",
      "Case #18: 0.000000\n",
      "Case #19: 0.021137\n",
      "Case #20: 0.001047\n",
      "Case #21: 1.000000\n",
      "Case #22: 0.014876\n",
      "Case #23: 1.000000\n",
      "Case #24: 1.000000\n",
      "Case #25: 0.065907\n",
      "Case #26: 0.001373\n",
      "Case #27: 0.001571\n",
      "Case #28: 0.000362\n",
      "Case #29: 0.017263\n",
      "Case #30: 0.303908\n",
      "Case #31: 0.000088\n",
      "Case #32: 0.000638\n",
      "Case #33: 0.000922\n",
      "Case #34: 0.000478\n",
      "Case #35: 0.005647\n",
      "Case #36: 0.006609\n",
      "Case #37: 0.000504\n",
      "Case #38: 0.000071\n",
      "Case #39: 0.004132\n",
      "Case #40: 0.071207\n",
      "Case #41: 0.000946\n",
      "Case #42: 0.000823\n",
      "Case #43: 0.000623\n",
      "Case #44: 0.080932\n",
      "Case #45: 1.000000\n",
      "Case #46: 0.000532\n",
      "Case #47: 0.000000\n",
      "Case #48: 0.000605\n",
      "Case #49: 0.000000\n",
      "Case #50: 0.000311\n",
      "Case #51: 0.333300\n",
      "Case #52: 0.000000\n",
      "Case #53: 0.016642\n",
      "Case #54: 0.278907\n",
      "Case #55: 0.002340\n",
      "Case #56: 0.000000\n",
      "Case #57: 0.202983\n",
      "Case #58: 0.016485\n",
      "Case #59: 0.006768\n",
      "Case #60: 0.041402\n",
      "Case #61: 0.150757\n",
      "Case #62: 0.717563\n",
      "Case #63: 0.999900\n",
      "Case #64: 0.000343\n",
      "Case #65: 0.002337\n",
      "Case #66: 0.000341\n",
      "Case #67: 0.004728\n",
      "Case #68: 0.562500\n",
      "Case #69: 0.001893\n",
      "Case #70: 0.172905\n",
      "Case #71: 0.000895\n",
      "Case #72: 0.000272\n",
      "Case #73: 0.000597\n",
      "Case #74: 0.000000\n",
      "Case #75: 0.101721\n",
      "Case #76: 0.000917\n",
      "Case #77: 1.000000\n",
      "Case #78: 0.000000\n",
      "Case #79: 0.000287\n",
      "Case #80: 0.000872\n",
      "Case #81: 0.069262\n",
      "Case #82: 0.023512\n",
      "Case #83: 0.833300\n",
      "Case #84: 0.000000\n",
      "Case #85: 0.001683\n",
      "Case #86: 0.003738\n",
      "Case #87: 0.000503\n",
      "Case #88: 0.995012\n",
      "Case #89: 0.034427\n",
      "Case #90: 1.000000\n",
      "Case #91: 0.015728\n",
      "Case #92: 1.000000\n",
      "Case #93: 0.000574\n",
      "Case #94: 0.002420\n",
      "Case #95: 0.082127\n",
      "Case #96: 0.003190\n",
      "Case #97: 0.000000\n",
      "Case #98: 0.000228\n",
      "Case #99: 0.000643\n",
      "Case #100: 0.007091\n"
     ]
    }
   ],
   "source": [
    "parse(open(\"C:\\Users\\mheik\\Downloads\\C-small-1-attempt0.in\"))"
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
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
