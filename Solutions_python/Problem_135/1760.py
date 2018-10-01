#!/usr/bin/python3
from sys import argv

def main(args):
    with open(args[1]) as f, open(args[2], 'w') as out:
        cases = int(f.readline())
        for case in range(0, cases):
            c1 = int(f.readline())
            nums1 = set()
            for i in range(1, 5):
                line = f.readline()
                if i == c1:
                    nums1 = {int(x) for x in line.split()}

            c2 = int(f.readline())
            nums2 = set()
            for i in range(1, 5):
                line = f.readline()
                if i == c2:
                    nums2 = {int(x) for x in line.split()}

            out.write('Case #%d: ' % (case + 1))
            inter = nums1.intersection(nums2)
            if len(inter) == 0:
                out.write('Volunteer cheated!')
            elif len(inter) > 1:
                out.write('Bad magician!')
            else:
                out.write('%d' % (inter.pop()))
            out.write('\n')

if __name__ == '__main__':
    main(argv)
        

