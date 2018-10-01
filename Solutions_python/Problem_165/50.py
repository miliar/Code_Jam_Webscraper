{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cases = [] \n",
    "with open('A-large.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        r, c, w = map(int, f.readline().split())\n",
    "        cases.append((r, c, w))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ret = []\n",
    "for i, (r, c, w) in enumerate(cases):\n",
    "    x = (c // w) * r + w - 1\n",
    "    if c % w != 0:\n",
    "        x += 1\n",
    "    ret.append('Case #%s: %s' % (i + 1, x))"
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
    "with open('A-large.out', 'w') as f:\n",
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
   "version": "2.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
