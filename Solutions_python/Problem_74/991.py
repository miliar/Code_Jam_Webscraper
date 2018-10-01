input = open('A-large.in','r');
output = open('output.txt','w');

nrTestCases = int(input.readline());

line = input.readline().strip('\n');
case = 1;
while line != '':

    positions = {'O' : 1, 'B' : 1};
    goals = {'O' : [], 'B' : []};
    allGoals = [];
    values = line.split(' ');
    nrButtons = int(values[0]);

    for i in range(nrButtons):
        bot = values[ 2*i + 1]
        position = int(values[2*i + 2 ])
        allGoals.append(bot)
        if bot == 'O':
            goals['O'].append(position)
        else:
            goals['B'].append(position)

    nextGoals = {'O' : None, 'B' : None}
    if len(goals['O']) > 0:
        nextGoals['O'] = goals['O'].pop(0);
    
    if len(goals['B']) > 0:
        nextGoals['B'] = goals['B'].pop(0);

    totalTime = 0;
    if len(allGoals) > 0:
        currentBot = allGoals.pop(0);
    else:
        currentBot = None;

    while currentBot != None:
        diffs = {'O' : 0, 'B' : 0}
        if nextGoals['O'] != None:
            diffs['O'] = positions['O'] - nextGoals['O'];

        if nextGoals['B'] != None:
            diffs['B'] = positions['B'] - nextGoals['B'];
        if diffs[currentBot] == 0:
            currentTime = 1;           
        else:    
            currentTime = abs(diffs[currentBot]);
        totalTime += currentTime;    
    
        if currentBot == 'O':
            if diffs['O'] == 0:
                # push button
                if len(goals['O']) > 0:
                    nextGoals['O'] = goals['O'].pop(0);
                else:
                    nextGoals['O'] = None;
                if len(allGoals) > 0:
                    currentBot = allGoals.pop(0);
                else:
                    currentBot = None;

                if diffs['B'] != 0:
                    if diffs['B'] > 0:
                        positions['B'] -= 1;
                    else:
                        positions['B'] += 1;
            else:
                # walk robot
                positions['O'] = nextGoals['O'];
                if diffs['B'] != 0:
                    if abs(diffs['B']) <= abs(diffs['O']):
                        positions['B'] = nextGoals['B'];
                    else:
                        if diffs['B'] > 0:
                            positions['B'] -= abs(diffs['O']);
                        else:
                            positions['B'] += abs(diffs['O']);
        else:
            if diffs['B'] == 0:
                # push button
                if len(goals['B']) > 0:
                    nextGoals['B'] = goals['B'].pop(0);
                else:
                    nextGoals['B'] = None;
                if len(allGoals) > 0:
                    currentBot = allGoals.pop(0);
                else:
                    currentBot = None;

                if diffs['O'] != 0:
                    if diffs['O'] > 0:
                        positions['O'] -= 1;
                    else:
                        positions['O'] += 1;
            else:
                # walk robot
                positions['B'] = nextGoals['B'];
                if diffs['O'] != 0:
                    if abs(diffs['O']) <= abs(diffs['B']):
                        positions['O'] = nextGoals['O'];
                    else:
                        if diffs['O'] > 0:
                            positions['O'] -= abs(diffs['B']);
                        else:
                            positions['O'] += abs(diffs['B']);
           
        
    output.write('Case #%d: %d\n' % (case, totalTime));
    case += 1;
    line = input.readline().strip('\n');
