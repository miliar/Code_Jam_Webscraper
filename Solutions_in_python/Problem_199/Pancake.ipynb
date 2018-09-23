{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "# store power of 2\n",
    "pow2 = []\n",
    "for i in xrange(0, 1005):\n",
    "    pow2.append(2**i)\n",
    "    \n",
    "def getFlips(var, panSize):\n",
    "    var = var[::-1]\n",
    "    start = 0\n",
    "    for i, bit in enumerate(var):\n",
    "        bit = 1 if bit =='+' else 0\n",
    "        start += bit*pow2[i]\n",
    "\n",
    "    mask = pow2[panSize] - 1\n",
    "    bitChecker = 1\n",
    "    curIdx = 0\n",
    "    length = len(var)\n",
    "    flips = 0\n",
    "    zerosSoFar = 0\n",
    "    \n",
    "    while(curIdx < length):\n",
    "        if(bitChecker & start) == 0:\n",
    "            zerosSoFar += 1\n",
    "            # look ahead\n",
    "            if ( (bitChecker * 2) & start > 0) or (zerosSoFar == panSize):\n",
    "                start = start ^ mask\n",
    "                mask = mask * pow2[zerosSoFar]\n",
    "                zerosSoFar = 0\n",
    "                flips += 1\n",
    "        else:\n",
    "            mask *= 2\n",
    "            \n",
    "        bitChecker *= 2\n",
    "        curIdx += 1\n",
    "    \n",
    "    if zerosSoFar > 0:\n",
    "        start = start ^ mask\n",
    "        flips += 1\n",
    "\n",
    "    expected = pow2[length]-1 \n",
    "    return flips if expected == start else 'IMPOSSIBLE'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "3\n",
      "2\n",
      "1\n",
      "3\n",
      "IMPOSSIBLE\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "print(getFlips('+++------+++---', 3))\n",
    "print(getFlips('---+-++-', 3))\n",
    "print(getFlips('--++++--', 2))\n",
    "print(getFlips('++++++--', 2))\n",
    "print(getFlips('----++--', 2))\n",
    "print(getFlips('-+-+-', 2))\n",
    "print(getFlips('+++++', 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "54\n"
     ]
    }
   ],
   "source": [
    "var = ''\n",
    "numPossible = 0\n",
    "for i in xrange(0, 1000):\n",
    "    var = ''\n",
    "    for j in xrange(0, 1000):\n",
    "        rand = random.random()\n",
    "        var += '+' if rand > 0.5 else '-'\n",
    "\n",
    "    if getFlips2(var, 5) != 'IMPOSSIBLE':\n",
    "        numPossible += 1\n",
    "\n",
    "print(numPossible)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "results = []\n",
    "with open('data/pancake/small.txt') as f:\n",
    "    lines = list(f)\n",
    "    l = len(lines)\n",
    "    for l in lines[1:l]:\n",
    "        var = l.split(' ')[0]\n",
    "        size = int(l.split(' ')[1])\n",
    "        results.append(getFlips(var, size))\n",
    "        \n",
    "with open('data/pancake/small_result.txt', 'w') as f:\n",
    "    for i, r in enumerate(results):\n",
    "        f.write('Case #'+str(i+1)+': '+str(r)+'\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "results = []\n",
    "with open('data/pancake/large.txt') as f:\n",
    "    lines = list(f)\n",
    "    l = len(lines)\n",
    "    for l in lines[1:l]:\n",
    "        var = l.split(' ')[0]\n",
    "        size = int(l.split(' ')[1])\n",
    "        results.append(getFlips(var, size))\n",
    "        \n",
    "with open('data/pancake/large_result.txt', 'w') as f:\n",
    "    for i, r in enumerate(results):\n",
    "        f.write('Case #'+str(i+1)+': '+str(r)+'\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
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
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
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
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "python3.6.1",
   "language": "python",
   "name": "python3.6.1"
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
 "nbformat_minor": 0
}
