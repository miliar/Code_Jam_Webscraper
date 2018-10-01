{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# File names\n",
    "f_in_name = \"B-large.in\"\n",
    "f_out_name = \"B-large_out.txt\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Just flip each one\n",
    "\n",
    "f_in = open(f_in_name)\n",
    "lines = f_in.readlines()\n",
    "f_in.close\n",
    "\n",
    "# Solve each test case\n",
    "answers = []\n",
    "n_cases = int(lines[0])\n",
    "for line in lines[1:]:\n",
    "    \n",
    "    ## SOLVE PROBLEM\n",
    "    ##################\n",
    "    num = line.strip()\n",
    "    num = list(num)\n",
    "    num = [int(c) for c in num]\n",
    "    \n",
    "    digits_reversed = list(reversed(num))\n",
    "    for i in range(len((digits_reversed[:-1]))):\n",
    "        d = digits_reversed[i]\n",
    "        if d < digits_reversed[i+1]:\n",
    "            digits_reversed[i+1] -= 1\n",
    "            for j in range(i+1):\n",
    "                digits_reversed[j] = 9\n",
    "    \n",
    "    tidy_num = \"\".join(str(i) for i in reversed(digits_reversed))\n",
    "    tidy_num = int(tidy_num)\n",
    "    answers.append(tidy_num)\n",
    "        \n",
    "# Write to file\n",
    "f_out = open(f_out_name, 'w')\n",
    "for i, a in enumerate(answers):\n",
    "    f_out.write(\"Case #{}: {}\\n\".format(i+1, a))\n",
    "f_out.close()"
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
   "display_name": "Python [conda env:py35]",
   "language": "python",
   "name": "conda-env-py35-py"
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
 "nbformat_minor": 2
}
