{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "IOError",
     "evalue": "[Errno 2] No such file or directory: 'C-large.in'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIOError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-70bbfcfe3089>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mget_ipython\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_cell_magic\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mu'time'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34mu''\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34mu\"from collections import defaultdict\\ndef split(N):\\n    if N%2 == 1:\\n        return (N-1)/2, (N-1)/2\\n    else:\\n        return (N-1)/2, (N-1)/2 + 1\\ncnt = 0\\ndef solve(N, K):\\n    global cnt\\n    rooms = defaultdict(int)\\n    rooms[N] = 1\\n    while K:\\n        #print rooms\\n        cnt += 1\\n        assert(len(rooms.keys())<=3)\\n        biggest = max(rooms.keys())\\n        new_rooms = split(biggest)\\n        K -= rooms[biggest]\\n        \\n        if K <= 0:\\n            return max(new_rooms), min(new_rooms)\\n            \\n        rooms[new_rooms[0]] += rooms[biggest]\\n        rooms[new_rooms[1]] += rooms[biggest]\\n        rooms.pop(biggest)\\n        \\ninfile = open('C-large.in')\\noutfile = open('out.txt', 'w')\\n\\nT = int(infile.readline())\\nfor t in range(1, T+1):\\n    N, K = map(int, infile.readline().split())\\n    a, b = solve(N, K)\\n    outfile.write('Case #{}: {} {}\\\\n'.format(t, a, b))\\n\\ninfile.close()\\noutfile.close()\\n            \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mC:\\IntelPython27\\lib\\site-packages\\IPython\\core\\interactiveshell.pyc\u001b[0m in \u001b[0;36mrun_cell_magic\u001b[1;34m(self, magic_name, line, cell)\u001b[0m\n\u001b[0;32m   2118\u001b[0m             \u001b[0mmagic_arg_s\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvar_expand\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstack_depth\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2119\u001b[0m             \u001b[1;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbuiltin_trap\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2120\u001b[1;33m                 \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmagic_arg_s\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcell\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2121\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2122\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<decorator-gen-61>\u001b[0m in \u001b[0;36mtime\u001b[1;34m(self, line, cell, local_ns)\u001b[0m\n",
      "\u001b[1;32mC:\\IntelPython27\\lib\\site-packages\\IPython\\core\\magic.pyc\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(f, *a, **k)\u001b[0m\n\u001b[0;32m    191\u001b[0m     \u001b[1;31m# but it's overkill for just that one bit of state.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    192\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mmagic_deco\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 193\u001b[1;33m         \u001b[0mcall\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mlambda\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    194\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    195\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mcallable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\IntelPython27\\lib\\site-packages\\IPython\\core\\magics\\execution.pyc\u001b[0m in \u001b[0;36mtime\u001b[1;34m(self, line, cell, local_ns)\u001b[0m\n\u001b[0;32m   1175\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1176\u001b[0m             \u001b[0mst\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mclock2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1177\u001b[1;33m             \u001b[1;32mexec\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mglob\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlocal_ns\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1178\u001b[0m             \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mclock2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1179\u001b[0m             \u001b[0mout\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<timed exec>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mIOError\u001b[0m: [Errno 2] No such file or directory: 'C-large.in'"
     ]
    }
   ],
   "source": [
    "%%time\n",
    "from collections import defaultdict\n",
    "def split(N):\n",
    "    if N%2 == 1:\n",
    "        return (N-1)/2, (N-1)/2\n",
    "    else:\n",
    "        return (N-1)/2, (N-1)/2 + 1\n",
    "cnt = 0\n",
    "def solve(N, K):\n",
    "    global cnt\n",
    "    rooms = defaultdict(int)\n",
    "    rooms[N] = 1\n",
    "    while K:\n",
    "        #print rooms\n",
    "        cnt += 1\n",
    "        assert(len(rooms.keys())<=3)\n",
    "        biggest = max(rooms.keys())\n",
    "        new_rooms = split(biggest)\n",
    "        K -= rooms[biggest]\n",
    "        \n",
    "        if K <= 0:\n",
    "            return max(new_rooms), min(new_rooms)\n",
    "            \n",
    "        rooms[new_rooms[0]] += rooms[biggest]\n",
    "        rooms[new_rooms[1]] += rooms[biggest]\n",
    "        rooms.pop(biggest)\n",
    "        \n",
    "infile = open('C-large.in')\n",
    "outfile = open('out.txt', 'w')\n",
    "\n",
    "T = int(infile.readline())\n",
    "for t in range(1, T+1):\n",
    "    N, K = map(int, infile.readline().split())\n",
    "    a, b = solve(N, K)\n",
    "    outfile.write('Case #{}: {} {}\\n'.format(t, a, b))\n",
    "\n",
    "infile.close()\n",
    "outfile.close()\n",
    "            "
   ]
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
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
