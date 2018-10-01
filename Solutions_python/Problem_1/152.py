import string
name='A-large'
fileinput=open(name+'.in' ,'r')
input=fileinput.read().splitlines()
fileinput.close()
fileoutput=open(name+'.out' ,'w')
cases=int(input[0])
i=0
for case in range(0,cases):
    server={}
    search=[]
    switch=[]
    debugoutput = '\nCase #'+str(case+1)+':\nservers: '
    i+=1
    numberofservers = int(input[i])
    for j in range(0, numberofservers):
        i+=1
        server[input[i]]=j
        debugoutput += str(server[input[i]])+input[i]+','

    debugoutput += '\nsearches: '
    servertemp = server.values()
    i+=1
    numberofsearches = int(input[i])
    for j in range(0, numberofsearches):
        i+=1
        s=server[input[i]]
        search.append(s)
        if s in servertemp:
            servertemp.remove(s)
            if servertemp.__len__()==0:
                #if switch[switch.__len__()-1] != servertemp[0]:
                switch.append(s)
                debugoutput += '(' + str(s) + ')'
                servertemp = server.values()
                servertemp.remove(s)

        debugoutput += str(search[j])

    print debugoutput+'=('+str(switch.__len__())+')'
    fileoutput.write('Case #' + str(case+1) + ': ' + str(switch.__len__()) + '\n')
fileoutput.close()
