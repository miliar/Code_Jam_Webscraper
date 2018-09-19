from qualification.alient_language import AlienLanguage
import unittest
class TestAlienLanguage(unittest.TestCase):
    def setUp(self):
        self.input_file_name = "A-large.in"
#        self.input_file_name = "alient_language_input.txt"
        
    def tearDown(self):
        pass
    
#    def test_parse_LDN(self):
#        al = AlienLanguage(self.input_file_name)
#        self.assertEquals(3, al.L)
#        self.assertEquals(5, al.D)
#        self.assertEquals(4, al.N)
#    
#    def test_input_words(self):
#        al = AlienLanguage(self.input_file_name)
#        expected = ['abc','bca','dac','dbc','cba']
#        self.assertEquals(expected, al.input_words)
#    
#    def test_sample_cases_parsing(self):
#        al = AlienLanguage(self.input_file_name)
#        expected = ['(ab)(bc)(ca)','abc','(abc)(abc)(abc)','(zyx)bc']
#        self.assertEquals(expected, al.samples)
#    
#    def test_convert_sample_to_list(self):
#        self.assertEquals(['ab','c','d'], AlienLanguage.convert_sample_to_list('(ab)cd'))
#        self.assertEquals(['ab','bcd'], AlienLanguage.convert_sample_to_list('(ab)(bcd)'))
#        self.assertEquals(['ab','bcd','d','abb'], AlienLanguage.convert_sample_to_list('(ab)(bcd)d(abb)'))
        
#    def test_get_total_probable_list(self):
#        self.assertEquals(['acd','bcd'],AlienLanguage.get_total_probable_list(['ab','c','d'], 3))
#        self.assertEquals(['acd', 'aed', 'bcd', 'bed', 'fcd', 'fed'],AlienLanguage.get_total_probable_list(['abf','ce','d'], 3))
#        self.assertEquals(18, len(AlienLanguage.get_total_probable_list(['abf','ce','dxy'], 3)))
#        self.assertEquals(72, len(AlienLanguage.get_total_probable_list(['abf','ce','dxy','ouyt'], 4)))
    
    def test_final(self):
        al = AlienLanguage(self.input_file_name)
        y = '\n'.join(al.solve())
        open('out-large.txt','w').write(y)

if __name__ == "__main__": 
    unittest.main()