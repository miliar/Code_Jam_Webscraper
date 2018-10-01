input = open('B-large.in','r');
output = open('output.txt','w');

nrTestCases = int(input.readline());

line = input.readline().strip('\n');
case = 1;
while line != '':
    
    values = line.split(' ');
    nrCombines = int(values[0])
    combines = {};
    for i in range(nrCombines):
        combines[values[i + 1][0:2]] = values[i + 1][2];

    nrOpposes = int(values[nrCombines + 1]);
    opposes = [];
    for i in range(nrOpposes):
        opposes.append(values[i + 2 + nrCombines]);

    nrBaseElements = int(values[nrCombines + nrOpposes + 2]);
    baseElements = values[nrCombines + nrOpposes + 3]

    elementList = [];
    for i in range(nrBaseElements):
        newElement = baseElements[i];
        lenEL = len(elementList);
        if lenEL > 0:
            c1 =  newElement + elementList[lenEL - 1]
            c2 =  elementList[lenEL - 1] + newElement
            combine = None;
            if c1 in combines:            
                combine = combines[c1];
            elif c2 in combines:
                combine = combines[c2];
            if combine != None:
                elementList[lenEL - 1] = combine;
                continue;
            else:
                elementList.append(newElement);

            # has not been combined
            for j, element in enumerate(elementList):
                c1 = newElement + element;                
                c2 = element + newElement;
                oppose = False;
                if c1 in opposes or c2 in opposes:
                    oppose = True;
                if oppose:
                    elementList = [];
                    break;
        else:
            elementList.append(newElement);
    elStr = "%s" % elementList
    elStr = elStr.replace('\'','');
    output.write('Case #%d: %s\n' % (case, elStr));
    case += 1;
    line = input.readline().strip('\n');
    
