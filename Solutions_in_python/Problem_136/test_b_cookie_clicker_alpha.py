from unittest import TestCase
from codejam2014.a_magic_trick import AMagicTrick
from codejam2014.b_cookie_clicker_alpha import BCookieClickerAlpha
from codejam2014.functions import *

__author__ = 'tehsphinx'


class TestB(TestCase):
    file_prefix = 'b_'

    def setUp(self):
        pass

    def disable_test_sample(self):
        file_suffix = '_sample'

        mt = BCookieClickerAlpha(self.file_prefix + 'input' + file_suffix, self.file_prefix + 'output' + file_suffix)
        result = mt.process()

        dbg(result)
        should_be = {
            1: 'Case #1: 1.0',
            2: 'Case #2: 39.1666667',
            3: 'Case #3: 63.9680013',
            4: 'Case #4: 526.1904762',
        }

        self.assertDictEqual(result, should_be)

    def disable_test_run_process(self):
        """
        rename to test_run_process to execute the real thing. input has to be in a_input.txt. output will be in a_output.txt
        """
        file_suffix = ''

        mt = BCookieClickerAlpha(self.file_prefix + 'input' + file_suffix, self.file_prefix + 'output' + file_suffix)
        mt.process()

    def test_run_process_large(self):
        """
        rename to test_run_process to execute the real thing. input has to be in a_input.txt. output will be in a_output.txt
        """
        file_suffix = '_large'

        mt = BCookieClickerAlpha(self.file_prefix + 'input' + file_suffix, self.file_prefix + 'output' + file_suffix)
        mt.process()

