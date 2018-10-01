{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "---+-++- 3\n",
      "Case #1: 3\n",
      "+++++ 4\n",
      "Case #2: 0\n",
      "-+-+- 4\n",
      "Case #3: IMPOSSIBLE\n"
     ]
    }
   ],
   "source": [
    "t = int(input())\n",
    "for i in range(1, t + 1):\n",
    "    S, K = input().split(\" \")\n",
    "    S = [1 if _=='+' else 0 for _ in S]\n",
    "    K = int(K)\n",
    "    ans = 0\n",
    "    for l in range(len(S)-K+1):\n",
    "        if S[l]&1:\n",
    "            continue\n",
    "        ans += 1\n",
    "        for j in range(K):\n",
    "            S[l+j] += 1\n",
    "    for j in range(K):\n",
    "        if not S[l+j]&1:\n",
    "            ans = 'IMPOSSIBLE'\n",
    "    print(\"Case #{}: {}\".format(i, ans))"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
