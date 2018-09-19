import sys, collections

input = open('B-large.in')
#input = open('B-large-practice.in')
#output = sys.stdout
output = open('B-large.out','w')
    
def myread():
    return input.readline().rstrip("\n\r")

def int_ize(an_array):
    return map(lambda x: int(x), an_array)

def main():
    n_cases = int(input.readline())
    
    case_no = 1
    while case_no <= n_cases:
        case_result = solve_case()
        output.write("Case #%d: %s\n" % (case_no, case_result))
        case_no+=1
    
def solve_case():
    dancers = int_ize(myread().split(" "))
    N = dancers[0]
    S = dancers[1]
    p = dancers[2]
    dancers = dancers[3:]
    
    # Special cases
    if p == 0:
        return N
    
    count_normal = 0
    count_surprising = 0
    break_value = p*3-2
    for score in dancers:
        if score >= break_value:
            count_normal+=1
        elif score >= max(break_value-2,p):
            count_surprising+=1
   
    return count_normal + min(count_surprising,S)

main()
