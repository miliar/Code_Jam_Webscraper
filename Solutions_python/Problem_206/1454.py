{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f = open('AL.in','r')\n",
    "g = open('bath4.txt','w')\n",
    "T = f.readline()\n",
    "for t in range(0,int(T)):\n",
    "    inp = f.readline().replace(\"\\n\",\"\")\n",
    "    D = int(inp.split(\" \")[0])\n",
    "    N = int(inp.split(\" \")[1])\n",
    "    max_time = 0\n",
    "    for i in range(N):\n",
    "        inp = f.readline().replace(\"\\n\",\"\")\n",
    "        ki = int(inp.split(\" \")[0])\n",
    "        si = int(inp.split(\" \")[1])\n",
    "        if (D-ki)/si >max_time:\n",
    "            max_time = (D-ki)/si\n",
    "    \n",
    "    g.write(\"Case #%s: %f\" % (t+1, D/max_time))\n",
    "    if t!=int(T)-1:\n",
    "        g.write(\"\\n\")"
   ]
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
 "nbformat_minor": 1
}
