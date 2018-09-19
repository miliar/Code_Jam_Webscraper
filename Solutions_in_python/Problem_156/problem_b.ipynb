{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Problem B. Infinite House of Pancakes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cache = {}"
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
    "cases = [] \n",
    "with open('B-small-attempt1.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        d = int(f.readline())\n",
    "        panc = map(int, f.readline().strip().split())\n",
    "        assert d == len(panc)\n",
    "        cases.append(panc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(panc):\n",
    "    panc = sorted(panc, reverse=True)\n",
    "    if 0 in panc:\n",
    "        panc = panc[:panc.index(0)]\n",
    "    if not panc:\n",
    "        return 0\n",
    "    if panc[0] <= 3:\n",
    "        return panc[0]\n",
    "    panc = tuple(panc)\n",
    "    if panc not in cache:\n",
    "        opts = [solve(map(lambda x: x - 1, panc))]\n",
    "        for i in range(len(panc)):\n",
    "            if panc[i] > 3:\n",
    "                val = panc[i]\n",
    "                for diff in range(2, val / 2 + 1):\n",
    "                    poss = list(panc)\n",
    "                    poss[i] = diff\n",
    "                    poss.append(val - diff)\n",
    "                    opts.append(solve(poss))\n",
    "        x = min(opts) + 1\n",
    "        cache[panc] = x            \n",
    "    return cache[panc]    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "ret = []\n",
    "for i, case in enumerate(cases):\n",
    "    x = solve(case)\n",
    "    ret.append('Case #%s: %s' % (i + 1, x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('B-small-attempt1.out', 'w') as f:\n",
    "    for line in ret:\n",
    "        f.write(line + '\\n')"
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
   "language": "python",
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
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
