'''
Created on Apr 13, 2012

@author: Irving
'''

class tongues(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.file = open('C:\Users\Irving\Downloads\A-small-attempt3.in', 'r')
        self.output = open('C:\Users\Irving\Desktop\output.in', 'w')
        self.googToEng = {"a":"y", "b":"h", "c":"e", "d":"s", "e":"o", "f":"c",
                          "g":"v", "h":"x", "i":"d", "j":"u", "k":"i", "l":"g",
                          "m":"l", "n":"b", "o":"k", "p":"r", "q":"z", "r":"t",
                          "s":"n", "t":"w", "u":"j", "v":"p", "w":"f", "x":"m",
                          "y":"a", "z":"q", " ":" "}
    
    def convert(self):
        first = True
        case = 1
        engList = []
        for line in self.file:
            if first:
                first = False
            else:
                sentence = "Case #" + str(case) + ": "
                goog = list(line)
                for character in goog:
                    if character != '\n':
                        engList.append(self.googToEng[character])
                eng = ''.join(engList)
                sentence = sentence + eng + "\n"
                case = case + 1
                engList = []
                self.output.write(sentence)
        self.output.close()
          
if __name__ == "__main__":
    translater = tongues()
    translater.convert()

        
            
            
        
        