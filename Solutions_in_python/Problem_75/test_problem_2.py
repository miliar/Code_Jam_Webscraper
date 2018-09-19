import unittest

from magicka import Invokator, parse_line

class InvokeElementsTestCase(unittest.TestCase):

    def test_can_create_a_invoke(self):
        invokator = Invokator()

    def test_should_be_set_a_combinations_for_invokator(self):
        invokator = Invokator(combination='RIR')
        self.assertEqual('RIR', invokator.combination)

    def test_should_be_set_a_opposet_elements_for_invokator(self):
        invokator = Invokator(opposed='FE')
        self.assertEqual('FE', invokator.opposed)

    def test_invokator_should_be_invoke_a_element(self):
        invokator = Invokator()
        invokator.invoke('E')
        invokator.invoke('A')
        self.assertEqual('[E, A]', invokator.elements)

    def test_list_with_combine_elements(self):
        invokator = Invokator(combination='QRI')
        invokator.invoke('R')
        invokator.invoke('R')
        invokator.invoke('Q')
        invokator.invoke('R')
        self.assertEqual('[R, I, R]', invokator.elements)

    def test_list_with_opposed_and_combine_elements(self):
        invokator = Invokator(combination='EEZ', opposed='QE')
        invokator.invoke('Q')
        invokator.invoke('E')
        invokator.invoke('E')
        invokator.invoke('E')
        invokator.invoke('E')
        invokator.invoke('R')
        invokator.invoke('A')
        self.assertEqual('[Z, E, R, A]', invokator.elements)

    def test_list_with_opposed_elements(self):
        invokator = Invokator(opposed='QW')
        invokator.invoke('Q')
        invokator.invoke('W')
        self.assertEqual('[]', invokator.elements)

    def test_xpto(self):
        invokator = Invokator(combination='QFT', opposed='QF')
        invokator.invoke('F')
        invokator.invoke('A')
        invokator.invoke('Q')
        invokator.invoke('F')
        invokator.invoke('D')
        invokator.invoke('F')
        invokator.invoke('Q')
        self.assertEqual('[F, D, T]', invokator.elements)

    def test_1(self):
        invokator = Invokator(combination='QFT', opposed='RF')
        invokator.invoke('Q')
        invokator.invoke('F')
        self.assertEqual('[T]', invokator.elements)

    def test_2(self):
        invokator = Invokator(combination='QFT', opposed='RF')
        invokator.invoke('Q')
        invokator.invoke('E')
        invokator.invoke('F')
        self.assertEqual('[Q, E, F]', invokator.elements)

    def test_3(self):
        invokator = Invokator(combination='QFT', opposed='RF')
        invokator.invoke('R')
        invokator.invoke('F')
        invokator.invoke('E')
        self.assertEqual('[E]', invokator.elements)

    def test_4(self):
        invokator = Invokator(combination='QFT', opposed='RF')
        invokator.invoke('R')
        invokator.invoke('E')
        invokator.invoke('F')
        self.assertEqual('[]', invokator.elements)

    def test_5(self):
        invokator = Invokator(combination='QFT', opposed='RF')
        invokator.invoke('R')
        invokator.invoke('Q')
        invokator.invoke('F')
        self.assertEqual('[R, T]', invokator.elements)

    def test_6(self):
        invokator = Invokator(combination='QFT', opposed='RF')
        invokator.invoke('R')
        invokator.invoke('F')
        invokator.invoke('Q')
        self.assertEqual('[Q]', invokator.elements)

    def test_clared_list(self):
        invokator = Invokator(combination='WQP', opposed='WR')
        invokator.invoke('D')
        invokator.invoke('E')
        invokator.invoke('W')
        invokator.invoke('Q')
        invokator.invoke('W')
        invokator.invoke('D')
        invokator.invoke('Q')
        invokator.invoke('E')
        invokator.invoke('Q')
        invokator.invoke('R')
        self.assertEqual('[]', invokator.elements)

    def test_another_clared_list(self):
        invokator = Invokator(combination='QQL', opposed='SF')
        invokator.invoke('E')
        invokator.invoke('W')
        invokator.invoke('D')
        invokator.invoke('F')
        invokator.invoke('S')
        invokator.invoke('Q')
        invokator.invoke('Q')
        invokator.invoke('W')
        invokator.invoke('W')
        invokator.invoke('E')
        self.assertEqual('[L, W, W, E]', invokator.elements)

class ParseLineTestCase(unittest.TestCase):

    def test_parse_can_returns_a_sequence(self):
        self.assertEqual((None, None, 'EA'), parse_line('0 0 2 EA'))

    def test_parse_can_returns_a_sequence2(self):
        self.assertEqual(('QRI', None, 'RRQR'), parse_line('1 QRI 0 4 RRQR'))

    def test_parse_can_returns_a_sequence3(self):
        self.assertEqual(('QFT', 'QF', 'FAQFDFQ'), parse_line('1 QFT 1 QF 7 FAQFDFQ'))

    def test_parse_can_returns_a_sequence4(self):
        self.assertEqual(('EEZ', 'QE', 'QEEEERA'), parse_line('1 EEZ 1 QE 7 QEEEERA'))

    def test_parse_can_returns_a_sequence5(self):
        self.assertEqual((None, 'QW', 'QW'), parse_line('0 1 QW 2 QW'))


unittest.main()
