import pandas as pd
def parse_input(inp_file):
    cases = []
    with open(inp_file) as f:
        num_cases = int(f.readline()[:-1])
        for i in range(num_cases):
            tmp = f.readline()
            if "\n" in tmp:
                tmp = tmp[:-1]
            #print tmp
            L, X = map(int,tmp.split(" "))
            inp_str= f.readline()[:-1]
            cases.append([L, X , inp_str])
    return cases

qm = {
    '1' : { '1' : '1',    'i': 'i' ,   'j' : 'j',    'k' : 'k' } ,
    'i' : { '1' : 'i',   'i': '-1',   'j' : 'k',    'k' : '-j' } ,
    'j' : { '1' : 'j',    'i': '-k',   'j' : '-1',   'k' : 'i' } ,
    'k' : { '1' : 'k',    'i': 'j' ,   'j' : '-i',   'k' : '-1' } ,
    }


def dijkstra(cases):
    with open('data.out', 'w') as f:
        for i,case in enumerate(cases):
            #f.write("-------------------------\n")
            #f.write("%s  %s \n"%(case[0] , case [1]))
            ret =  exec_case(case)
            f.write("Case #%d: %s\n" %(i+1,ret))
            #print "Case #%d: %s\n" %(i+1,ret)
            #f.write("-------------------------\n")
    f.close()


def exec_case(case):
    L , X , inp_str = case
    #print L, X , inp_str
    X = X%4 + (4 if X > 4 else 0)
    tot_len = len(inp_str*X)
    if evaluate(inp_str*X)!='-1':
        return "NO"
    for aa in range(1,tot_len-1):
        i = evaluate((inp_str*X)[:aa])
        if i != 'i':
            continue
        for bb in range(aa+1, tot_len):
            #print aa, bb
            j = evaluate((inp_str*X)[aa:bb])
            if j !='j':
                continue
            k = evaluate((inp_str*X)[bb:])
            if k =='k':
                #print (inp_str*X)[:aa], (inp_str*X)[aa:bb] , (inp_str*X)[bb:]
                return "YES"
    return "NO"

def evaluate(inp):
    neg_count = 0
    prev = inp[0]
    for i in range(1,len(inp)):
        prev = qm[prev][inp[i]]
        if prev[0] == '-':
            neg_count = neg_count + 1
            prev = prev[1]
        
    if neg_count %2 ==0:
        return prev
    else:
        return "-"+prev
        
    
if __name__ == '__main__':
    cases = parse_input('data.in')
    dijkstra(cases)
    #print evaluate("ijk")
