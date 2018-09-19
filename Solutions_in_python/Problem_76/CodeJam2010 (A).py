#!/usr/bin/python
# -*- coding: utf-8 -*-

import operator
FILENAME = r'C-large'

class Program:
    def main( self, args ):
        numCases = 0

        textReader = open('%s.in'  % (FILENAME,), 'r')
        textWriter = open('%s.out' % (FILENAME,), 'w')

        numCases = int( textReader.readline() )

        for caseNumber in xrange( 1, numCases + 1 ):

            N = textReader.readline().strip()

            nums = [int(x) for x in textReader.readline().strip().split(' ')]

            result = nums[0]
            for i in nums[1:]:
                result = operator.xor( result, i )

            #print nums

            if result != 0:
                textWriter.write('Case #%d: %s\n' % (caseNumber, "NO"))
            else:
                MIN = min(nums)
                SUM = sum(nums)
                answer = SUM - MIN
                textWriter.write('Case #%d: %s\n' % (caseNumber, str(answer)))

        textReader.close()
        textWriter.close()


# Run the program is this file is executed (versus imported)
if __name__ == '__main__':
    import sys
    program = Program()
    sys.exit( program.main( sys.argv ) )
