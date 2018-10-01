{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "i_f = open('C-small-2-attempt1.in', 'r')\n",
    "o_f = open('outputC-small2.txt', 'w')\n",
    "t = int(i_f.readline())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    (n,k) = i_f.readline().split(\" \")  # read a list of integers, 2 in this case\n",
    "    (a,b) = solve(int(n),int(k))\n",
    "    o_f.write(\"Case #{}: {} {}\\n\".format(i, a, b))\n",
    "o_f.close()\n",
    "i_f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(n,k):\n",
    "    l = {}\n",
    "    l[n] = 1\n",
    "    for i in range(k):\n",
    "        m = max(l.keys())\n",
    "        if (l[m]==1):\n",
    "            l.pop(m,None)\n",
    "        else:\n",
    "            l[m]-=1\n",
    "        m1 = (m-1)//2\n",
    "        m2 = m - 1 - m1\n",
    "        if (m1 in l.keys()):\n",
    "            l[m1] +=1\n",
    "        else:\n",
    "            l[m1] = 1\n",
    "        if (m2 in l.keys()):\n",
    "            l[m2] +=1\n",
    "        else:\n",
    "            l[m2] = 1\n",
    "    return (m2,m1)"
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
