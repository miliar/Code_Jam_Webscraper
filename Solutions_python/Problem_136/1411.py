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
        case.farmCost, case.farmOutput, case.win = [ float(i) for i in Input.file.readline().strip('\n').split(' ') ]
        return case


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


class Output:
    @staticmethod
    def log(result):
        try:
            Output.file==None
        except:
            Output.file=open('solution.txt','w')
            Output.index=0
        Output.index+=1
        result=' '.join([str(i) for i in result])
        result='Case #'+str(Output.index)+': '+result
        print(result)
        Output.file.write(result+'\n')


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


class Case:
    def __str__(self):
        output=[]
        for i in set(dir(self))-(set(dir(Case()))):
            output.append(str(i)+" : "+str(getattr(self, i)))
        return '\n'.join(output)

    def time_to_win(self,farm):
        return self.win/(2.0+self.farmOutput*farm)

    def time_to_farm(self, farm):
        return self.farmCost/(2.0+self.farmOutput*farm)

    def addFarm(self,farm):
        addTime=self.time_to_win(farm)
        addFarmTime=self.time_to_farm(farm)+self.time_to_win(farm+1)

        return addFarmTime<addTime

    def solve(self):
        print(str(self))

        time=0.0
        farm=0
        while self.addFarm(farm)==True:
            time+=self.time_to_farm(farm)
            farm+=1
        time+=self.time_to_win(farm)

        return [time]


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


def main():
    caseCount = Input.parse()
    for case in Input.case():
        result = case.solve()
        Output.log(result)

main()