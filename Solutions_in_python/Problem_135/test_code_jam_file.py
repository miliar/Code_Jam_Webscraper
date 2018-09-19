from unittest import TestCase
from codejam2014.code_jam_file import CodeJamFile
from codejam2014.functions import *

__author__ = 'tehsphinx'


class TestCodeJamFile(TestCase):
    def setUp(self):
        pass

    def test_process_cases(self):
        mt = CodeJamFile('input_sample', case_length=10)
        mt.process_file()

        should_be = {1: ['2', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16', '3', '1 2 5 4', '3 11 6 15', '9 10 7 12', '13 14 8 16'], 2: ['2', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16', '2', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16'], 3: ['2', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16', '3', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16']}
        self.assertDictEqual(mt.cases, should_be)


