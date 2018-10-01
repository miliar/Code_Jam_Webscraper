{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# N == number of FREE SHIT PLACES\n",
    "# K == number of ETHERNAL SHIT TAKERS\n",
    "import math\n",
    "\n",
    "## note N and K are both long valued\n",
    "def shitAssignment(N, K):\n",
    "    level = math.floor(math.log2(K))\n",
    "    \n",
    "    ## gaps is a 2 d array = [(bigger_gap length, number of those), (smaller_gap length, number of those)]\n",
    "    gaps = calculateGaps(N, level)\n",
    "    \n",
    "    levelIndex = K - int(math.pow(2,level))\n",
    "    \n",
    "    return calculateMinMax(gaps, levelIndex)"
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
    "def calculateGaps(F, levelNumber):\n",
    "    ## gaps is a 2 d array = [(bigger_gap length, number of those), (smaller_gap length, number of those)]\n",
    "    result = [(F,1)]\n",
    "    \n",
    "    for level in range(0, levelNumber):\n",
    "        result = updateResult(result)\n",
    "        \n",
    "    return result\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def updateResult(result):\n",
    "    temp = []\n",
    "    \n",
    "    for i in range(0, len(result)):\n",
    "        if result[i][0]//2 != result[i][0]/2:\n",
    "            # if result[0][0] is odd --> only one type of branching\n",
    "            temp.append(tuple([(result[i][0]-1)//2, 2*result[i][1]]))\n",
    "        else:\n",
    "            temp.append(tuple([(result[i][0])//2, result[i][1]]))\n",
    "            temp.append(tuple([(result[i][0]-1)//2,result[i][1]]))\n",
    "        \n",
    "    return consolidate(temp)  \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def consolidate(temp):\n",
    "    result = []\n",
    "    tempHash = {}\n",
    "    \n",
    "    for mmbr in temp:\n",
    "        if mmbr[0] in tempHash:\n",
    "            tempHash[mmbr[0]] += mmbr[1]\n",
    "        else:\n",
    "            tempHash[mmbr[0]] = mmbr[1]\n",
    "    \n",
    "    for key in tempHash:\n",
    "        if key>0:\n",
    "            result.append(tuple([key, tempHash[key]]))\n",
    "    \n",
    "    return result\n",
    "    \n",
    "    "
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
    "def calculateMinMax(gaps, levelIndex):\n",
    "    \n",
    "    # the first of menas that you have certainly destroyed the all bigger gaps -- > only small geps remained\n",
    "    if levelIndex+1 > gaps[0][1]:\n",
    "        if gaps[1][0]//2 != gaps[1][0]/2:\n",
    "            return (gaps[1][0]-1)//2, (gaps[1][0]-1)//2\n",
    "        else:\n",
    "            return (gaps[1][0])//2, (gaps[1][0]-1)//2\n",
    "    else:\n",
    "        if gaps[0][0]//2 != gaps[0][0]/2:\n",
    "            return (gaps[0][0]-1)//2, (gaps[0][0]-1)//2\n",
    "        else:\n",
    "            return (gaps[0][0])//2, (gaps[0][0]-1)//2\n",
    "        "
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
    "collapsed": true
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
    "#  reading in the arguments of the code executable\n",
    "fin_name = \"C-small-2-attempt0.in.txt\"\n",
    "fout_name = \"smallTwo.txt\"\n",
    "\n",
    "# opening the output file for writing\n",
    "fout = open(fout_name, 'w')\n",
    "\n",
    "#  reading all lines at once from the opened file\n",
    "with open(fin_name, 'r') as fin:\n",
    "    \n",
    "    lines = fin.readlines()\n",
    "\n",
    "# T - number of test casess\n",
    "T = int(lines[0].split()[0])\n",
    "\n",
    "for test_case in range(1, T+1):\n",
    "    input_variable_array = lines[test_case].split()\n",
    "\n",
    "    output_string = shitAssignment(int(input_variable_array[0]), int(input_variable_array[1]))\n",
    "    fout.write(\"Case #\" + str(test_case) + \": \" + str(output_string[0]) + \" \" + str(output_string[1])  + \"\\n\")\n",
    "\n",
    "fin.close()\n",
    "fout.close()\n"
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
 "nbformat_minor": 0
}
