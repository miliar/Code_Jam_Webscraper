cases = 0
class Cosa:
    caseNumber = 0
    pancakes = ""
    paleta = 0
    movimientos = 0

    def __init__(self, useCase, caseNumber):

        useCase = useCase.rstrip()
        cosa = useCase.split()
        self.pancakes = cosa[0]
        self.paleta = int(cosa[1])
        self.caseNumber = caseNumber

    def getMinMovements(self):
        None

    def turnSigns(self):
        index = self.pancakes.find("-")
        if index >= 0:
            if len(self.pancakes) - index >= self.paleta:
                for x in range(index, index + self.paleta):
                    s = list(self.pancakes)
                    c = self.pancakes[x]
                    if c == "+":
                        s[x] = "-"
                    else:
                        s[x] = "+"
                    self.pancakes = "".join(s)
                self.movimientos += 1
                self.turnSigns()
            else:
                self.movimientos = -1

    def getMovementsString(self):
        if self.movimientos >= 0:
            return str(self.movimientos)
        else:
            return "IMPOSSIBLE"

    def __str__(self):
        return "Case #" + str(self.caseNumber) + ": " + self.getMovementsString()


file = open("cosa.in", "r")
i = 0

newFileString = ""

for line in file:
    i += 1
    if i == 1:
        cases = line
    else:
        cosa = Cosa(line, i-1)
        cosa.turnSigns()
        newFileString += str(cosa) + "\n"

newFileString = newFileString[:-1]
print newFileString

text_file = open("Output.txt", "w")
text_file.write(newFileString)
text_file.close()


