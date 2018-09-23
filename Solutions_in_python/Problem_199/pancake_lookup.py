from __future__ import print_function
import csv

lookup_dict = {k: {} for k in range(2, 11)}
with open('skd.csv', 'rb') as csvfile:
    myreader = csv.reader(csvfile, delimiter=' ')
    for row in myreader:
        k, s, d = row
        k = int(k)
        d = int(d)
        print(k, s, d)
        lookup_dict[k][s] = d

for k in lookup_dict.keys():
    for s in lookup_dict[k].keys():
        d = lookup_dict[k][s]
        print(k, s, d)

def lookup(s, k):
    try:
        return str(lookup_dict[k][s])
    except KeyError:
        return 'IMPOSSIBLE'

if __name__ == '__main__':


    samples = [
        ('++', 2),
        ('+++', 2),
        ('++++', 2),
        ('+++++', 2),
        ('++++++', 2),
        ('+++++++', 2),
        ('+'*10, 5),
        ('++++', 3),
        ('+++++', 3),
        ('+++++', 4),
        ('---+-++-', 3),
        ('+++++', 4),
        ('-+-+-', 4),
        ('---+-++++', 3),
        ('---+-++++', 2),
        ('---+-++++', 4),
    ]

    for sample in samples:
        print(lookup(*sample))

    data_files = ['A-small-attempt0',]
                #   'A-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for in_ in inputs:
                line = tuple([_ for _ in in_.split(' ')])
                s = line[0]
                k = int(line[1])
                output_file.write('Case #{0}: {1}\n'.format(i, lookup(s, k)))
                i += 1
