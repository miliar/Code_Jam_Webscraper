{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "d = np.array([[1, 2], [0, 2], [0, 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "d[0][::-1].sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4, 3, 2, 1])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = np.array([1,2,3,4])\n",
    "a[::-1].sort()\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "h = np.array([2, 3, 1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 3, 1])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "h"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(h[d[0]] == h[1]).any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(in_file, out_file):\n",
    "    d = np.array([[1, 2], [0, 2], [0, 1]])\n",
    "    to_str = ['R','Y','B']\n",
    "    \n",
    "    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:\n",
    "        T = int(fin.readline().strip())\n",
    "        for t in range(1, T+1):\n",
    "            N, r, o, y, g, b, v = map(int, fin.readline().strip().split(' '))\n",
    "            num_h = np.array([r, y, b]) # r = 0, y = 1, b = 2\n",
    "            \n",
    "            res = np.zeros(N, dtype=np.int8)\n",
    "            \n",
    "            # set the first horse\n",
    "            most_pop = h.argmax()\n",
    "            res[0] = most_pop\n",
    "            num_h[most_pop] -= 1\n",
    "            \n",
    "            # set the rest\n",
    "            for p in range(1, N):\n",
    "#                 print(res[p-1])\n",
    "                n1, n2 = d[res[p-1]]\n",
    "                \n",
    "                if num_h[n1] > num_h[n2]:\n",
    "                    res[p] = n1\n",
    "                    num_h[n1] -= 1\n",
    "                elif num_h[n2] > num_h[n1]:\n",
    "                    res[p] = n2\n",
    "                    num_h[n2] -= 1\n",
    "                elif num_h[n1] == 0: # == num_h[n2]\n",
    "                    break\n",
    "                elif n1 == res[0]:  # it's a tie, put the one that IS the first\n",
    "                    res[p] = n1\n",
    "                    num_h[n1] -= 1\n",
    "                else:\n",
    "                    res[p] = n2\n",
    "                    num_h[n2] -= 1\n",
    "            \n",
    "            if (num_h > 0).any() or res[0] == res[-1]:\n",
    "                print('IMPOSSIBLE')\n",
    "                print('IMPOSSIBLE', file=fout)\n",
    "            else: # valid result\n",
    "                string_res = ''.join(map(lambda h: to_str[h], res))\n",
    "                print('Case #{t}: {r}'.format(t=t, r=string_res))\n",
    "                print('Case #{t}: {r}'.format(t=t, r=string_res), file=fout)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: YBRYBR\n",
      "IMPOSSIBLE\n",
      "Case #3: YRBRYBRYBR\n"
     ]
    }
   ],
   "source": [
    "solve('horse.in', 'horse.out')"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
