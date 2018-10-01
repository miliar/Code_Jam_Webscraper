import unittest
import math
from bathroom_stalls import TreeNode


class MyTestCase(unittest.TestCase):

    def test5(self):
        tree = TreeNode(5)

        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())


    def test10(self):
        tree = TreeNode(10)

        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())
        print(tree.visit())


    def test10_2(self):
        tree = TreeNode(10)

        print(tree.visit_k(3))


if __name__ == '__main__':
    unittest.main()
