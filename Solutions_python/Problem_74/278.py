def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for it in (item for item in seq if f(item)):
        return it

class BotIdentities:
    BLUE=1
    ORANGE=2

class Instruction:
    """An instruction"""

    def __init__(self, botId, position):
        self.botId = botId
        self.position = position

class Bot:
    """A Bot"""

    def __init__(self, identity):
        """Initialisation"""
        self.identity = identity
        self.position = 1
        self.target = self.getNextTarget()

    def getNextTarget(self):
        instruction = find(lambda i: i.botId == self.identity, instructions)
        if instruction:
            pos = instruction.position
        else:
            pos = 0
        return pos

    def takeAStep(self, pushAllowed):
        pushedButton = False

        if self.position < self.target:
            self.position = self.position + 1

        elif self.position > self.target:
            self.position = self.position - 1

        elif pushAllowed and self.identity == instructions[0].botId:
            instructions.pop(0)
            self.target = self.getNextTarget()
            pushedButton = True

        return pushedButton

class Overseer:
    """Manages the bots"""

    def __init__(self):
        firstInstruction = instructions[0]
        if firstInstruction.botId == BotIdentities.ORANGE:
            self.bot1 = Bot(BotIdentities.ORANGE)
            self.bot2 = Bot(BotIdentities.BLUE)
        else:
            self.bot1 = Bot(BotIdentities.BLUE)
            self.bot2 = Bot(BotIdentities.ORANGE)

    def makeAMove(self):
        pushed = self.bot1.takeAStep(True)
        self.bot2.takeAStep(not pushed)

    def countMoves(self):
        moves = 0
        while instructions:
            self.makeAMove()
            moves = moves + 1

        return moves

instructionFile = open("instructions.txt", "r").readlines()
caseNo = 1
for line in instructionFile:
    instructions = []
    thisId = None
    for word in line.split():
        if word == "O":
            thisId = BotIdentities.ORANGE
        elif word == "B":
            thisId = BotIdentities.BLUE
        elif thisId:
            posn = int(word)
            instruction = Instruction(thisId, posn)
            thisId = None
            instructions.append(instruction)

    if instructions:
        overseer = Overseer()
        moves = overseer.countMoves()
        print("Case #", caseNo, ": ", moves, sep="")
        caseNo = caseNo + 1
