from manager import Manager
        
class SIT(Manager):

    def main(self):
        mapping = {
            'y' : 'a',
            'n' : 'b',
            'f' : 'c',
            'i' : 'd',
            'c' : 'e',
            'w' : 'f',
            'l' : 'g',
            'b' : 'h',
            'k' : 'i',
            'u' : 'j',
            'o' : 'k',
            'm' : 'l',
            'x' : 'm',
            's' : 'n',
            'e' : 'o',
            'v' : 'p',
            'z' : 'q',
            'p' : 'r',
            'd' : 's',
            'r' : 't',
            'j' : 'u',
            'g' : 'v',
            't' : 'w',
            'h' : 'x',
            'a' : 'y',
            'q' : 'z',
            ' ' : ' '
        }
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            line = self.input.readline().strip()
            for token in line:
                self.output.write(mapping[token])
            self.output.write("\n")
        self.output.close()
        
program = SIT('/home/ezequiel/Descargas/A-small-attempt1.in')
program.main()
