{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def SliceRow(myrow):\n",
    "    row = list(myrow)\n",
    "    fill = '?'\n",
    "    tokenLetter = '?'\n",
    "    tokenIdx = -1\n",
    "    n = len(row)\n",
    "    for i in range(n):\n",
    "        if row[i] == '?':\n",
    "            row[i] = fill\n",
    "        else:\n",
    "            fill = row[i]\n",
    "            if tokenLetter == '?':\n",
    "                tokenLetter = fill\n",
    "                tokenIdx = i\n",
    "    if tokenLetter != '?':\n",
    "        for i in range(tokenIdx):\n",
    "            row[i] = tokenLetter\n",
    "    if tokenLetter == '?':\n",
    "        finish = 0\n",
    "    else:\n",
    "        finish = 1\n",
    "    return (''.join(row), finish)\n",
    "\n",
    "def SliceCake(cake):\n",
    "    r = len(cake)\n",
    "    c = len(cake[0])\n",
    "    RowFill = [0] * r\n",
    "    FillCake = [cake[_] for _ in range(r)]\n",
    "    for i in range(r):\n",
    "        FillCake[i], RowFill[i] = SliceRow(cake[i])\n",
    "    tokenRow = '?' * c\n",
    "    # find the to be filled row index\n",
    "    for i in range(r):\n",
    "        if RowFill[i] == 1:\n",
    "            firstFilledRowIdx = i\n",
    "            break\n",
    "    for i in range(r):\n",
    "        if RowFill[i] == 1:\n",
    "            tokenRow = FillCake[i]\n",
    "        else:\n",
    "            FillCake[i] = tokenRow\n",
    "    for i in range(firstFilledRowIdx):\n",
    "        FillCake[i] = FillCake[firstFilledRowIdx]\n",
    "    return FillCake        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "inputPath = \"Prob-A/A-small-attempt0.in\"\n",
    "outputPath = \"Prob-A/A-small-attempt0.txt\"\n",
    "f = open(inputPath, 'r')\n",
    "g = open(outputPath, 'w')\n",
    "numCase = int(f.readline().strip())\n",
    "for k in range(numCase):\n",
    "    r, c = f.readline().strip().split(' ')\n",
    "    r = int(r)\n",
    "    c = int(c)\n",
    "    cake = []\n",
    "    for i in range(r):\n",
    "        cake.append(f.readline().strip())\n",
    "    res = SliceCake(cake)\n",
    "    #print(res)\n",
    "    g.write('Case #' + str(k + 1) + ':\\n')\n",
    "    for i in range(r):\n",
    "        g.write(res[i] + '\\n')\n",
    "g.close()\n",
    "    "
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
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
