{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import itertools\n",
    "nrange = lambda stop: iter(itertools.count().next, stop)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Patrick\\\\Documents'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
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
    "def read_input(fn):\n",
    "    with open(fn, 'r') as f:\n",
    "        lines = f.readlines()\n",
    "        num_in = int(lines[0])\n",
    "    return num_in, map(lambda l: l.strip(), lines[1:])\n",
    "\n",
    "def write_output(solutions, out_fn):\n",
    "    with open(out_fn, 'w') as f:\n",
    "        i = 0\n",
    "        for sol in solutions:\n",
    "            i += 1\n",
    "            f.write(\"Case #{i}: {solution}\\n\".format(i=i, solution=sol))\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def p1(k, s):\n",
    "    flips = 0\n",
    "    head = 0\n",
    "    while (head + k) <= len(s):\n",
    "        #print head, s\n",
    "        if s[head]:\n",
    "            head += 1\n",
    "            continue\n",
    "        \n",
    "        for i in nrange(k):\n",
    "            #print head, flips, i\n",
    "            s[head + i] = not s[head + i]\n",
    "            \n",
    "        flips += 1\n",
    "        head += 1\n",
    "    \n",
    "    if all(s):\n",
    "        return str(flips)\n",
    "    else:\n",
    "        return \"IMPOSSIBLE\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "p1_file = \"A-large.in\"\n",
    "_num_in, inputs = read_input(p1_file)\n",
    "\n",
    "#print inputs\n",
    "sols = []\n",
    "for in_line in inputs:\n",
    "    #print in_line\n",
    "    s, k = in_line.split(\" \")\n",
    "    sols.append(p1(int(k), [(c == '+') for c in s]))\n",
    "                    \n",
    "                    \n",
    "write_output(sols, \"p1_s.txt\")"
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
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def p2(n):\n",
    "    digits = map(int, str(n))\n",
    "    for i in nrange(len(digits) - 1):\n",
    "        if any(digits[i] > tail for tail in digits[i+1:]):\n",
    "            digits[i] -= 1\n",
    "            for j in nrange(i+1, len(digits)):\n",
    "                digits[j] = 9\n",
    "    return int(\"\".join(map(str, digits)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n"
     ]
    }
   ],
   "source": [
    "_num_in, inputs = read_input('p2.in')\n",
    "write_output((p2(int(n_str)) for n_str in inputs), 'p2_s.out')\n",
    "print len(inputs)"
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
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def p3_2(stall_num, users):\n",
    "    gaps = {stall_num: 1}\n",
    "    while users > 0:\n",
    "        next_size = max(gaps.iterkeys())\n",
    "        empty = next_size - 1\n",
    "        ls, rs = empty / 2, (empty + 1)/2\n",
    "        if gaps[next_size] >= users:\n",
    "            return rs, ls\n",
    "        \n",
    "        if rs > 0:\n",
    "            if rs in gaps:\n",
    "                gaps[rs] += gaps[next_size]\n",
    "            else:\n",
    "                gaps[rs] = gaps[next_size]\n",
    "                \n",
    "            if ls > 0:\n",
    "                if ls in gaps:\n",
    "                    gaps[ls] += gaps[next_size]\n",
    "                else:\n",
    "                    gaps[ls] = gaps[next_size]\n",
    "        \n",
    "        users -= gaps[next_size]\n",
    "        del gaps[next_size]\n",
    "        \n",
    "    return -1, -1\n",
    "    "
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n"
     ]
    }
   ],
   "source": [
    "_num_in, inputs = read_input('p3_large.in')\n",
    "\n",
    "write_output(\n",
    "    (' '.join(map(str, p3_2(int(n), int(k))))\n",
    "     for n, k in map(lambda in_str: map(int, in_str.split(' ')), inputs)), \n",
    "    'p3_s.out')\n",
    "\n",
    "\n",
    "print len(inputs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "max() arg is an empty sequence",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-20-53ebffdf7ae1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mN\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mK\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrandom\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrandrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m     \u001b[1;32mif\u001b[0m \u001b[0mp3\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mN\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mK\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mp3_2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mN\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mK\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m         \u001b[1;32mprint\u001b[0m \u001b[1;34m\"OH NO\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-11-5cf4b6496ebd>\u001b[0m in \u001b[0;36mp3\u001b[0;34m(stall_num, users)\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mnrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0musers\u001b[0m \u001b[1;33m-\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m         \u001b[1;31m#print gaps\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m         \u001b[0msize\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmax\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgaps\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miterkeys\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m         \u001b[0mgaps\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0msize\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m-=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m         \u001b[0mempty\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msize\u001b[0m \u001b[1;33m-\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: max() arg is an empty sequence"
     ]
    }
   ],
   "source": [
    "import random\n",
    "for i in xrange(1000):\n",
    "    N = i + 1\n",
    "    K = random.randrange(i + 1)\n",
    "    if p3(N,K) != p3_2(N,K):\n",
    "        print \"OH NO\"\n",
    "    else:\n",
    "        print \"K\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 5)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p3(400, 56)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 5)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p3_2(400, 56)"
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
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
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
 "nbformat_minor": 1
}
