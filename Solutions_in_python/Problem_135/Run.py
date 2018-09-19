from Case import Case
from Input import Input
from Output import Output

def main():
    caseCount = Input.parse()
    for case in Input.case():
        result = case.solve()
        Output.log(result)

main()