{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T14:16:03.006971-04:00",
     "start_time": "2017-04-22T14:16:02.968551"
    }
   },
   "outputs": [],
   "source": [
    "basename = 'C-large'\n",
    "#basename = 'sample'\n",
    "input_file = basename + '.in'\n",
    "output_file = basename + '.out'\n",
    "\n",
    "datas = []\n",
    "with open(input_file) as fin:\n",
    "    T = int(fin.readline())\n",
    "    for t in range(T):\n",
    "        N, Q = [int(_) for _ in fin.readline().split()]\n",
    "        E, S = [], []\n",
    "        for i in range(N):\n",
    "            e, s = [int(_) for _ in fin.readline().split()]\n",
    "            E.append(e)\n",
    "            S.append(s)\n",
    "        D = [None for i in range(N)]\n",
    "        for i in range(N):\n",
    "            D[i] = [int(_) for _ in fin.readline().split()]\n",
    "        U, V = [], []\n",
    "        for i in range(Q):\n",
    "            u, v = [int(_) for _ in fin.readline().split()]\n",
    "            u -= 1\n",
    "            v -= 1\n",
    "            U.append(u)\n",
    "            V.append(v)\n",
    "        data = {\n",
    "            'N': N, 'Q': Q, 'E': E, 'S': S, 'D': D, 'U':U, 'V':V\n",
    "        }\n",
    "        datas.append(data)"
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
   "execution_count": 49,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T14:16:03.846126-04:00",
     "start_time": "2017-04-22T14:16:03.821342"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import copy\n",
    "def solve(data):\n",
    "    N = data['N']\n",
    "    D = data['D']\n",
    "    E = data['E']\n",
    "    S = data['S']\n",
    "    U = data['U']\n",
    "    V = data['V']\n",
    "    D = copy.deepcopy(D)\n",
    "    # min dist\n",
    "    for k in range(N):\n",
    "        for i in range(N):\n",
    "            for j in range(N):\n",
    "                if i != j and i != k and k != j and D[i][k] != -1 and D[k][j] != -1:\n",
    "                    _d = D[i][k] + D[k][j]\n",
    "                    if D[i][j] == -1 or _d < D[i][j]:\n",
    "                        D[i][j] = _d\n",
    "                        \n",
    "    # min time\n",
    "    T = copy.deepcopy(D)\n",
    "    for i in range(N):\n",
    "        for j in range(N):\n",
    "            T[i][j] = None\n",
    "            if D[i][j] != -1 and D[i][j] <= E[i]:\n",
    "                T[i][j] = D[i][j] * 1.0 / S[i]\n",
    "                \n",
    "          \n",
    "    for k in range(N):\n",
    "        for i in range(N):\n",
    "            for j in range(N):\n",
    "                if i != j and i != k and k != j and T[i][k] is not None and T[k][j] is not None:\n",
    "                    _d = T[i][k] + T[k][j]\n",
    "                    if T[i][j] is None or _d < T[i][j]:\n",
    "                        T[i][j] = _d      \n",
    "    \n",
    "    res = []\n",
    "    for u, v in zip(U, V):\n",
    "        res.append(T[u][v])\n",
    "        \n",
    "    return ' '.join('%.10f' % _ for _ in res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T14:16:11.376799-04:00",
     "start_time": "2017-04-22T14:16:09.999405"
    }
   },
   "outputs": [],
   "source": [
    "# need paralleing\n",
    "\n",
    "with open(output_file, 'w') as fout: \n",
    "    for t, data in enumerate(datas):\n",
    "        res = solve(data)\n",
    "        # print('Case #%d: %s' % (t + 1, res))\n",
    "        print('Case #%d: %s' % (t + 1, res), file=fout)"
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
