__author__ = 'ceciet'


def cookie_clicker():

    with open('file/B-large.in') as input_file, open('file/B-large.out', 'w') as output_file:
    #with open('file/testCase') as input_file, open('file/result', 'w') as output_file:
        testNum = input_file.readline().strip()
        testData = input_file.readlines()
        for i in range(0, int(testNum)):
            numbers = testData[i].strip().split()
            C = float(numbers[0])
            F = float(numbers[1])
            X = float(numbers[2])
            #print (C, F, X)
            costTime = 0
            currentSpeed = 2

            while X/currentSpeed > X/(currentSpeed + F) + C/currentSpeed:
                costTime += C/currentSpeed
                currentSpeed += F

            costTime += X/currentSpeed
            costTime = format(costTime, '.6f')
            output_file.write("Case #" + str(i+1) + ': ' + str(costTime) + '\n')



if __name__ == '__main__':

    cookie_clicker()


