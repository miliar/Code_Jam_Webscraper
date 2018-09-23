{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": true,
    "editable": true
   },
   "source": [
    "# Google Code Jam 2017 — Round 1A — problem A\n",
    "## User: jdemeyer\n",
    "\n",
    "This is a Jupyter notebook to be run with SageMath version 8.0.beta1 on a 64-bit GNU/Linux system. Although the precise version of SageMath probably does not matter that much."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "%%cython\n",
    "\n",
    "import os, sys, datetime, time\n",
    "from sage.rings.integer cimport Integer\n",
    "\n",
    "\n",
    "def log(msg):\n",
    "    sys.stderr.write(msg + \"\\n\")\n",
    "    sys.stderr.flush()\n",
    "\n",
    "\n",
    "class CodejamProblem(object):\n",
    "    def __init__(self, input):\n",
    "        self.inputlines = iter(input.splitlines())\n",
    "        self.cases = []\n",
    "    \n",
    "    def readline(self):\n",
    "        return next(self.inputlines)\n",
    "        \n",
    "    def readint(self):\n",
    "        return Integer(self.readline())\n",
    "\n",
    "    def readints(self):\n",
    "        return [Integer(x) for x in self.readline().split()]\n",
    "        \n",
    "    def solve(self, f=sys.stdout, raw=False):\n",
    "        for i, case in enumerate(self.cases, 1):\n",
    "            sig_check()\n",
    "            ans = self.solvecase(case)\n",
    "            if raw:\n",
    "                ans = repr(ans)\n",
    "            else:\n",
    "                ans = self.formatanswer(ans)\n",
    "            f.write(\"Case #{0}: {1}\\n\".format(i, ans))\n",
    "        f.flush()\n",
    "        \n",
    "    def solvecheck(self, output):\n",
    "        from StringIO import StringIO\n",
    "        out = StringIO()\n",
    "        self.solve(out)\n",
    "        assert out.getvalue() == output\n",
    "            \n",
    "    def formatanswer(self, ans):\n",
    "        return str(ans)\n",
    "\n",
    "    @classmethod\n",
    "    def precompute(cls):\n",
    "        pass\n",
    "    \n",
    "    @classmethod\n",
    "    def autosolve(cls, filein, fileout, *args, **kwds):\n",
    "        log(\"precomputing...\")\n",
    "        cls.precompute()\n",
    "\n",
    "        log(\"autosolving...\")\n",
    "\n",
    "        nexc = 0\n",
    "        while nexc < 10:\n",
    "            sig_check()\n",
    "            t0 = datetime.datetime.now()\n",
    "            try:\n",
    "                input = open(filein).read()\n",
    "            except IOError:\n",
    "                time.sleep(0.2)\n",
    "                continue\n",
    "            d = datetime.datetime.now() - t0\n",
    "            log(\"Read input in %.2fs\" % d.total_seconds())\n",
    "            \n",
    "            t0 = datetime.datetime.now()\n",
    "            try:\n",
    "                problem = cls(input, *args, **kwds)\n",
    "            except Exception:\n",
    "                from traceback import print_exc\n",
    "                print_exc(file=sys.stderr)\n",
    "                nexc += 1\n",
    "                time.sleep(0.5)\n",
    "                continue\n",
    "            d = datetime.datetime.now() - t0\n",
    "            ncases = len(problem.cases)\n",
    "            log(\"Parsed input in %.2fs, got %s cases\" % (d.total_seconds(), ncases))\n",
    "            \n",
    "            t0 = datetime.datetime.now()\n",
    "            with open(fileout, 'w') as out:\n",
    "                problem.solve(out)\n",
    "            d = datetime.datetime.now() - t0\n",
    "            log(\"Solved problem in %.2fs\" % d.total_seconds())\n",
    "\n",
    "            problem.notify()\n",
    "            return\n",
    "        \n",
    "    @staticmethod\n",
    "    def notify():\n",
    "        os.system(\"mplayer /usr/share/apps/kgoldrunner/themes/default/victory.ogg >/dev/null\")\n",
    "\n",
    "\n",
    "class Problem(CodejamProblem):\n",
    "    def __init__(self, input):\n",
    "        CodejamProblem.__init__(self, input)\n",
    "        \n",
    "        T = self.readint()\n",
    "        for i in range(T):\n",
    "            R, C = self.readints()\n",
    "            rows = [list(self.readline()) for i in range(R)]\n",
    "            self.cases.append((R, C, rows))\n",
    "\n",
    "    def solvecase(self, case):\n",
    "        R, C, rows = case\n",
    "        # Expand rows\n",
    "        for r in rows:\n",
    "            prev = None\n",
    "            for i in range(len(r)):\n",
    "                letter = r[i]\n",
    "                if letter == '?':\n",
    "                    if prev is not None:\n",
    "                        r[i] = prev\n",
    "                else:\n",
    "                    if prev is None:\n",
    "                        for j in range(i):\n",
    "                            r[j] = letter\n",
    "                    prev = letter\n",
    "                    \n",
    "        # Expand cols\n",
    "        prev = None\n",
    "        for i in range(len(rows)):\n",
    "            r = rows[i]\n",
    "            if r[0] == '?':\n",
    "                if prev is not None:\n",
    "                    rows[i] = prev\n",
    "            else:\n",
    "                if prev is None:\n",
    "                    for j in range(i):\n",
    "                        rows[j] = r\n",
    "                prev = r\n",
    "                \n",
    "        return rows\n",
    "    \n",
    "    def formatanswer(self, rows):\n",
    "        ret = \"\"\n",
    "        for r in rows:\n",
    "            ret += \"\\n\" + \"\".join(r)\n",
    "        return ret"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "input=\"\"\"\n",
    "3\n",
    "3 3\n",
    "G??\n",
    "?C?\n",
    "??J\n",
    "3 4\n",
    "CODE\n",
    "????\n",
    "?JAM\n",
    "2 2\n",
    "CA\n",
    "KE\n",
    "\"\"\"\n",
    "\n",
    "output=\"\"\"\n",
    "Case #1:\n",
    "GGJ\n",
    "CCJ\n",
    "CCJ\n",
    "Case #2:\n",
    "CODE\n",
    "COAE\n",
    "JJAM\n",
    "Case #3:\n",
    "CA\n",
    "KE\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "input = \"\".join(line+\"\\n\" for line in input.splitlines() if line)\n",
    "output = \"\".join(line+\"\\n\" for line in output.splitlines() if line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "P = Problem(input)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: [['G', 'G', 'G'], ['C', 'C', 'C'], ['J', 'J', 'J']]\n",
      "Case #2: [['C', 'O', 'D', 'E'], ['C', 'O', 'D', 'E'], ['J', 'J', 'A', 'M']]\n",
      "Case #3: [['C', 'A'], ['K', 'E']]\n",
      "Case #1: \n",
      "GGG\n",
      "CCC\n",
      "JJJ\n",
      "Case #2: \n",
      "CODE\n",
      "CODE\n",
      "JJAM\n",
      "Case #3: \n",
      "CA\n",
      "KE\n"
     ]
    }
   ],
   "source": [
    "P.solve(raw=True)\n",
    "P.solve()\n",
    "#P.solvecheck(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "precomputing...\n",
      "autosolving...\n",
      "Read input in 0.00s\n",
      "Parsed input in 0.00s, got 100 cases\n",
      "Solved problem in 0.00s\n"
     ]
    }
   ],
   "source": [
    "P.autosolve(\"in/A-small-attempt0.in\", \"out\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "SageMath 8.0.beta2",
   "language": "",
   "name": "sagemath"
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
