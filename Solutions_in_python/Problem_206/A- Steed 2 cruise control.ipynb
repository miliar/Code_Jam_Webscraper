{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# File names\n",
    "f_in_name = \"A-large.in\"\n",
    "f_out_name = \"A large out.txt\""
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
    "# Input\n",
    "f_in = open(f_in_name)\n",
    "lines = f_in.readlines()\n",
    "f_in.close;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pdb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Solve each test case\n",
    "# pdb.set_trace()\n",
    "import itertools\n",
    "answers = []\n",
    "n_cases = int(lines[0])\n",
    "pos = 1\n",
    "for i, line in enumerate(lines):\n",
    "    \n",
    "    ## SOLVE PROBLEM\n",
    "    ##################\n",
    "    if i < pos:\n",
    "        continue\n",
    "        \n",
    "    # Read in test case's data\n",
    "    D, N = map(int, line.strip().split())\n",
    "    max_speed = 0.\n",
    "    pos = i+1+N\n",
    "    horse_list = []\n",
    "    slowest_horse = (0, 1e18)\n",
    "    for j in range(i+1, pos):\n",
    "        start_pos, speed = map(int, lines[j].strip().split())\n",
    "        if speed == slowest_horse[1]:\n",
    "            if start_pos < slowest_horse[0]:\n",
    "                slowest_horse = (start_pos, speed)\n",
    "        else:\n",
    "            meeting_time = (start_pos - slowest_horse[0]) / (slowest_horse[1] - speed)\n",
    "            meeting_dist = start_pos + meeting_time * speed\n",
    "            if meeting_time >= 0 and meeting_dist < D:\n",
    "                if speed < slowest_horse[1]:\n",
    "                    slowest_horse = (start_pos, speed)\n",
    "                    \n",
    "            # Finally check arrival times\n",
    "            slowest_horse_arrival_time = (D - slowest_horse[0]) / slowest_horse[1]\n",
    "            this_arrival_time = (D - start_pos) / speed\n",
    "            if this_arrival_time > slowest_horse_arrival_time:\n",
    "                slowest_horse = (start_pos, speed)\n",
    "                \n",
    "    # Find the arrival time of the last/slowest horse\n",
    "    arrival_time = (D - slowest_horse[0]) / slowest_horse[1]\n",
    "    speed_to_match = D / arrival_time   \n",
    "    answers.append(speed_to_match)      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
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
