{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Oversized Pancake Flipper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from pprint import pprint\n",
    "from IPython import embed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def decrement(N, i):\n",
    "    if N[i] == 0:\n",
    "        N[i] = 9\n",
    "        decrement(N, i - 1)\n",
    "    else:\n",
    "        N[i] -= 1\n",
    "    \n",
    "def get_first_inc_ind(N):\n",
    "    for i in range(len(N) - 1):\n",
    "        if N[i] > N[i + 1]:\n",
    "            return i\n",
    "    return None\n",
    "\n",
    "def solve(N):\n",
    "    first_inc_ind = get_first_inc_ind(N)\n",
    "    while first_inc_ind is not None:\n",
    "        # set all to max digit\n",
    "        for i in range(first_inc_ind + 1, len(N)):\n",
    "            N[i] = 9\n",
    "        # embed()\n",
    "        # decrement previous digits\n",
    "        decrement(N, first_inc_ind)\n",
    "        first_inc_ind = get_first_inc_ind(N)\n",
    "    N_int = 0\n",
    "    for i in range(len(N)):\n",
    "        N_int = N_int * 10 + N[i]\n",
    "    return N_int\n",
    "\n",
    "def run_test(test):\n",
    "    N = map(lambda ch: int(ch), test.strip())\n",
    "    return solve(N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "FILE_NAME = 'B-large'\n",
    "# FILE_NAME = 'A-large'\n",
    "INPUT_SUFFIX = '.in'\n",
    "OUTPUT_SUFFIX = '.out'\n",
    "\n",
    "INPUT_FILE = FILE_NAME + INPUT_SUFFIX\n",
    "OUTPUT_FILE = FILE_NAME + OUTPUT_SUFFIX\n",
    "\n",
    "with open(INPUT_FILE, 'r') as file_in:\n",
    "    lines = file_in.readlines()\n",
    "    T = lines[0]\n",
    "    tests = lines[1:]\n",
    "\n",
    "with open(OUTPUT_FILE, 'w') as file_out:\n",
    "    for i_test, test in enumerate(tests):\n",
    "        result = run_test(test)\n",
    "        file_out.write('Case #{}: {}\\n'.format(i_test + 1, result))"
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
