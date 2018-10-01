{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T02:03:31.066410-04:00",
     "start_time": "2017-04-08T02:03:31.055160"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import collections\n",
    "\n",
    "def div(v):\n",
    "    assert 1 <= v\n",
    "    if v % 2 == 1:\n",
    "        return v // 2, v // 2\n",
    "    else:\n",
    "        return v // 2, v // 2 - 1\n",
    "\n",
    "def solve(n, k):\n",
    "    c = collections.defaultdict(int)\n",
    "    c[n] = 1\n",
    "    while True:\n",
    "        v = max(c.keys())\n",
    "        assert v > 0\n",
    "        if k <= c[v]:\n",
    "            return '%d %d' % div(v)\n",
    "        else:\n",
    "            k -= c[v]\n",
    "            v1, v2 = div(v)\n",
    "            c[v1] += c[v]\n",
    "            c[v2] += c[v]\n",
    "            del c[v]\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T02:04:30.467282-04:00",
     "start_time": "2017-04-08T02:04:30.446899"
    }
   },
   "outputs": [],
   "source": [
    "input_filename = 'C-large.in'\n",
    "output_filename = 'C-large.out'\n",
    "\n",
    "inps = []\n",
    "with open(input_filename) as fin:\n",
    "    T = int(fin.readline())\n",
    "    for t in range(T):\n",
    "        inps.append([int(_) for _ in fin.readline().split()])\n",
    "    \n",
    "anss = []\n",
    "for n, k in inps:\n",
    "    ans = solve(n, k)\n",
    "    anss.append(ans)\n",
    "\n",
    "with open(output_filename, 'w') as fout:\n",
    "    for c, ans in enumerate(anss):\n",
    "        print('Case #%d: %s' % (c + 1, ans), file=fout)"
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
   "display_name": "Python ML (env35)",
   "language": "python",
   "name": "env35"
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
   "version": "3.5.3"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
