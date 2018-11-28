#include <stdio.h>
#include <iostream>
#include <string>
#include <QtCore>
#include <math.h>

QString solveCase(int n, int k) {
    QString answer;

    bool is = false;

    unsigned long long nOn = pow(2, n) - 1;
    for(int i = nOn; i <= k; i++) {
        if(i == k)
            is = true;
        i+= nOn;
    }

    if(is)
        return "ON";
    else
        return "OFF";

    return answer;
}

bool testExamples() {
    QString answer;

    std::cout << solveCase(2,2).toLatin1().data() << std::endl;
    std::cout << solveCase(1,1).toLatin1().data() << std::endl;
    std::cout << solveCase(4,0).toLatin1().data() << std::endl;
    std::cout << solveCase(4,47).toLatin1().data() << std::endl;

    if(solveCase(1,0) != "OFF")
        return false;
    else if(solveCase(1,1) != "ON")
        return false;
    else if(solveCase(4, 0) != "OFF")
        return false;
    else if(solveCase(4, 47) != "ON")
        return false;

    return true;
}

int main()
{
    if(testExamples()) {
        std::cout << "Examples Ok. Running true cases." << std::endl;
    }
    else {
        std::cout << "Examples have failed." << std::endl;
        return -1;
    }

    QString inputFilename = "A-large.in", outputFilename = "A-large.out";

    FILE *input = fopen(inputFilename.toLatin1().data(), "rb"), *output = fopen(outputFilename.toLatin1().data(), "wb");
    if(!input) {
        std::cout << "Could not open input file for reading. (" << inputFilename.toLatin1().data() << ")" << std::endl;
        return -1;
    }
    else if(!output) {
        std::cout << "Could not open output file for writing. (" << inputFilename.toLatin1().data() << ")" << std::endl;
        return -1;
    }
    else {
        int numCases = 0;
        fscanf(input, "%d", &numCases);

        for(int c = 0; c < numCases; c++) {
            int n, k;
            fscanf(input, "%d %d", &n, &k);
            fprintf(output, "Case #%d: %s\n", c+1, solveCase(n, k).toLatin1().data());
        }

        fclose(input);
        fclose(output);
    }

    return 0;
}
