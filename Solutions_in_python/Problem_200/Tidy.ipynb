{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# get data\n",
    "csvfile = open(\"tidy1.in\", 'r')\n",
    "reader = csv.reader(csvfile, delimiter=',')\n",
    "input_ = list(reader)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['132'],\n",
       " ['1000'],\n",
       " ['7'],\n",
       " ['879'],\n",
       " ['110'],\n",
       " ['257'],\n",
       " ['585'],\n",
       " ['550'],\n",
       " ['449'],\n",
       " ['887'],\n",
       " ['376'],\n",
       " ['176'],\n",
       " ['953'],\n",
       " ['441'],\n",
       " ['769'],\n",
       " ['821'],\n",
       " ['886'],\n",
       " ['999'],\n",
       " ['950'],\n",
       " ['519'],\n",
       " ['21'],\n",
       " ['795'],\n",
       " ['902'],\n",
       " ['213'],\n",
       " ['586'],\n",
       " ['684'],\n",
       " ['43'],\n",
       " ['900'],\n",
       " ['485'],\n",
       " ['100'],\n",
       " ['656'],\n",
       " ['693'],\n",
       " ['818'],\n",
       " ['530'],\n",
       " ['814'],\n",
       " ['428'],\n",
       " ['130'],\n",
       " ['451'],\n",
       " ['766'],\n",
       " ['913'],\n",
       " ['874'],\n",
       " ['747'],\n",
       " ['823'],\n",
       " ['194'],\n",
       " ['632'],\n",
       " ['128'],\n",
       " ['306'],\n",
       " ['654'],\n",
       " ['409'],\n",
       " ['819'],\n",
       " ['525'],\n",
       " ['205'],\n",
       " ['574'],\n",
       " ['788'],\n",
       " ['203'],\n",
       " ['215'],\n",
       " ['476'],\n",
       " ['263'],\n",
       " ['277'],\n",
       " ['87'],\n",
       " ['702'],\n",
       " ['411'],\n",
       " ['3'],\n",
       " ['440'],\n",
       " ['472'],\n",
       " ['32'],\n",
       " ['225'],\n",
       " ['541'],\n",
       " ['513'],\n",
       " ['518'],\n",
       " ['563'],\n",
       " ['52'],\n",
       " ['599'],\n",
       " ['507'],\n",
       " ['778'],\n",
       " ['534'],\n",
       " ['317'],\n",
       " ['841'],\n",
       " ['794'],\n",
       " ['326'],\n",
       " ['363'],\n",
       " ['265'],\n",
       " ['593'],\n",
       " ['231'],\n",
       " ['391'],\n",
       " ['882'],\n",
       " ['711'],\n",
       " ['242'],\n",
       " ['597'],\n",
       " ['714'],\n",
       " ['801'],\n",
       " ['688'],\n",
       " ['1'],\n",
       " ['196'],\n",
       " ['402'],\n",
       " ['351'],\n",
       " ['294'],\n",
       " ['344'],\n",
       " ['835'],\n",
       " ['740']]"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# parse data\n",
    "N = int(input_[0][0])\n",
    "data = input_[1:]\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def largest_non_decreasing_number(subnumber1, subnumber2, max_possible_last_number):\n",
    "    #print(subnumber1, subnumber2, max_possible_last_number)\n",
    "    length = len(subnumber1)\n",
    "    # stop criteria\n",
    "    if (length == 0):\n",
    "        return subnumber2\n",
    "    elif (length == 1):\n",
    "        digit = int(subnumber1)\n",
    "        if digit == 0:\n",
    "            return subnumber2\n",
    "        elif digit > max_possible_last_number:\n",
    "            digit -= 1\n",
    "            subnumber2 = \"\".join(['9'] * len(subnumber2))\n",
    "            if digit == 0:\n",
    "                return subnumber2\n",
    "            else:\n",
    "                return str(digit) + subnumber2\n",
    "        else:\n",
    "            return str(digit) + subnumber2\n",
    "    \n",
    "    # otherwise take last digit and compare it to second last\n",
    "    last = int(subnumber1[-1])\n",
    "    second_last = int(subnumber1[-2])\n",
    "    \n",
    "    # cases\n",
    "    if (last >= second_last):\n",
    "        # remove last number and obtain the highest one\n",
    "        subnumber1 = subnumber1[0:(length-1)]\n",
    "        subnumber2 = str(last) + subnumber2\n",
    "        max_possible_last_number = last\n",
    "    else:\n",
    "        # we need to decrease second last number and maximize the rest\n",
    "        second_last = second_last - 1\n",
    "        subnumber1 = subnumber1[0:(length-2)] + str(second_last)\n",
    "        last = 9\n",
    "        subnumber2 = \"\".join(['9'] * len(subnumber2)) # convert all subnumbers2 into '9'\n",
    "        subnumber2 = str(last) + subnumber2 # append last number\n",
    "        max_possible_last_number = 9\n",
    "    #print(\"created \" + subnumber1)\n",
    "    return largest_non_decreasing_number(subnumber1, subnumber2, max_possible_last_number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def largest_non_decreasing_number_wrapper(number):\n",
    "    number = str(number)\n",
    "    result = largest_non_decreasing_number(number, \"\", 9)\n",
    "    if (result == \"0\"):\n",
    "        return str(10**(len(number)-1) - 1)\n",
    "    else:\n",
    "        return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# run over all examples\n",
    "store = []\n",
    "for arr in data:\n",
    "    result = largest_non_decreasing_number_wrapper(arr[0])\n",
    "    store.append(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# write to file\n",
    "target = open(\"tidy.out\", 'w')\n",
    "for i in range(len(store)):\n",
    "    if i != 0:\n",
    "        target.write('\\n')\n",
    "    target.write('Case #' + str(i+1) + ': ' + store[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['129',\n",
       " '999',\n",
       " '7',\n",
       " '799',\n",
       " '99',\n",
       " '257',\n",
       " '579',\n",
       " '499',\n",
       " '449',\n",
       " '799',\n",
       " '369',\n",
       " '169',\n",
       " '899',\n",
       " '399',\n",
       " '699',\n",
       " '799',\n",
       " '799',\n",
       " '999',\n",
       " '899',\n",
       " '499',\n",
       " '19',\n",
       " '789',\n",
       " '899',\n",
       " '199',\n",
       " '579',\n",
       " '679',\n",
       " '39',\n",
       " '899',\n",
       " '479',\n",
       " '99',\n",
       " '599',\n",
       " '689',\n",
       " '799',\n",
       " '499',\n",
       " '799',\n",
       " '399',\n",
       " '129',\n",
       " '449',\n",
       " '699',\n",
       " '899',\n",
       " '799',\n",
       " '699',\n",
       " '799',\n",
       " '189',\n",
       " '599',\n",
       " '128',\n",
       " '299',\n",
       " '599',\n",
       " '399',\n",
       " '799',\n",
       " '499',\n",
       " '199',\n",
       " '569',\n",
       " '788',\n",
       " '199',\n",
       " '199',\n",
       " '469',\n",
       " '259',\n",
       " '277',\n",
       " '79',\n",
       " '699',\n",
       " '399',\n",
       " '3',\n",
       " '399',\n",
       " '469',\n",
       " '29',\n",
       " '225',\n",
       " '499',\n",
       " '499',\n",
       " '499',\n",
       " '559',\n",
       " '49',\n",
       " '599',\n",
       " '499',\n",
       " '778',\n",
       " '499',\n",
       " '299',\n",
       " '799',\n",
       " '789',\n",
       " '299',\n",
       " '359',\n",
       " '259',\n",
       " '589',\n",
       " '229',\n",
       " '389',\n",
       " '799',\n",
       " '699',\n",
       " '239',\n",
       " '589',\n",
       " '699',\n",
       " '799',\n",
       " '688',\n",
       " '1',\n",
       " '189',\n",
       " '399',\n",
       " '349',\n",
       " '289',\n",
       " '344',\n",
       " '799',\n",
       " '699']"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "store"
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
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
