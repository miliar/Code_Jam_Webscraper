import tongues

__author__ = 'dmorgant'

import unittest

input = "3\n\
ejp mysljylc kd kxveddknmc re jsicpdrysi\n\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n\
de kr kd eoya kw aej tysr re ujdr lkgc jv"

output = "Case #1: our language is impossible to understand\n\
Case #2: there are twenty six factorial possibilities\n\
Case #3: so it is okay if you want to just give up"

class TonguesTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(output, tongues.process(input))

if __name__ == '__main__':
    unittest.main()
