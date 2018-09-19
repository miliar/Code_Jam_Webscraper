from Case import Case

class Input:
    @staticmethod
    def parse():
        Input.file=open('problem.txt','r')
        Input.caseCount=int(Input.file.readline())

    @staticmethod
    def case():
        for i in range(0, Input.caseCount):
            yield Input.parseCase()

    @staticmethod
    def parseCase():
        case = Case()
        case.answer1=int(Input.file.readline())
        case.grid1=[]
        for row in range(0,4):
            case.grid1.append([ int(i) for i in Input.file.readline().strip('\n').split(' ') ])
        case.answer2=int(Input.file.readline())
        case.grid2=[]
        for row in range(0,4):
            case.grid2.append([ int(i) for i in Input.file.readline().strip('\n').split(' ') ])
        return case
