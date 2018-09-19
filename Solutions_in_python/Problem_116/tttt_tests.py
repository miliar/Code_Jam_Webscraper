import tttt
import unittest

class TestTTTT(unittest.TestCase):
    def test_example1(self):
        board = ["XXXT", "....", "OO..", "...."]
        self.assertEqual("X won", tttt.gameResult(board))

    def test_example2(self):
        board = ["XOXT", "XXOO", "OXOX", "XXOO"]
        self.assertEqual("Draw", tttt.gameResult(board))

    def test_example3(self):
        board = ["XOX.", "OX..", "....", "...."]
        self.assertEqual("Game has not completed", tttt.gameResult(board))

    def test_example4(self):
        board = ["OOXX", "OXXX", "OX.T", "O..O"]
        self.assertEqual("O won", tttt.gameResult(board))

    def test_example5(self):
        board = ["XXXO", "..O.", ".O..", "T..."]
        self.assertEqual("O won", tttt.gameResult(board))

    def test_example6(self):
        board = ["OXXX", "XO..", "..O.", "...O"]
        self.assertEqual("O won", tttt.gameResult(board))

if __name__ == '__main__':
    unittest.main(exit=False)
