import unittest
import math
from bathroom_stalls import Executor


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cut = Executor()

    def test1(self):
        self.assertEquals((1 ,0), self.cut.check_stalls(4, 2))

    def test2(self):
        self.assertEquals((1, 0), self.cut.check_stalls(5, 2))

    def test3(self):
        self.assertEquals((1, 1), self.cut.check_stalls(6, 2))


    def test4(self):
        self.assertEquals((2, 2), self.cut.check_stalls(5, 1))


    def test5(self):
        self.assertEquals((1, 0), self.cut.check_stalls(5,2))


    def test6(self):
        self.assertEquals((1, 0), self.cut.check_stalls(5, 3))


    def test7(self):
        self.assertEquals((0, 0), self.cut.check_stalls(5, 4))


    def test8(self):
        self.assertEquals((0, 0), self.cut.check_stalls(5, 5))


    def test9(self):
        self.assertEquals((5, 4), self.cut.check_stalls(10, 1))


    def test10(self):
        self.assertEquals((2, 2), self.cut.check_stalls(10, 2))


    def test11(self):
        self.assertEquals((2, 1), self.cut.check_stalls(10, 3))


    def test12(self):
        self.assertEquals((1, 0), self.cut.check_stalls(10, 4))


    def test12(self):
        self.assertEquals((0, 0), self.cut.check_stalls(10, 10))


if __name__ == '__main__':
    unittest.main()
