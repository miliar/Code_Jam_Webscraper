from unittest import TestCase
from codejam2014.a_magic_trick import AMagicTrick
from codejam2014.functions import *

__author__ = 'tehsphinx'


class TestAMagicTrick(TestCase):
    def setUp(self):
        pass

    def test_sample(self):
        file_suffix = '_sample'

        mt = AMagicTrick('input' + file_suffix, 'output' + file_suffix)
        result = mt.process()

        dbg(result)
        should_be = {
            1: 'Case #1: 7',
            2: 'Case #2: Bad magician!',
            3: 'Case #3: Volunteer cheated!',
        }

        self.assertDictEqual(result, should_be)

    def test_test_cases(self):

        file_suffix = '_test_cases'

        mt = AMagicTrick('input' + file_suffix, 'output' + file_suffix)
        result = mt.process()

        dbg(result)
        should_be = {
            1: 'Case #1: 7',
            2: 'Case #2: Bad magician!',
            3: 'Case #3: Volunteer cheated!',
            4: 'Case #4: 7',
        }

        self.assertDictEqual(result, should_be)

    def test_run_process(self):
        """
        rename to test_run_process to execute the real thing. input has to be in input.txt. output will be in output.txt
        """
        file_suffix = ''

        mt = AMagicTrick('input' + file_suffix, 'output' + file_suffix)
        mt.process()

