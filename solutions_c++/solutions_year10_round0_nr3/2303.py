#include <stdio.h>
#include <iostream>
#include <string>
#include <QtCore>

QString solveCase(int r, int k, QVector<int> groups) {
    QString answer;

    int money = 0;
    for(int i = 0; i < r; i++) {
        int ppl = 0;
        int gc;
        for(gc = 0; gc < groups.size(); gc++) {
            ppl += groups[gc];
            if(ppl > k) {
                ppl -= groups[gc];
                break;
            }
        }
        for(int j = 0; j < gc; j++) {
            int z = groups[0];
            groups.pop_front();
            groups.push_back(z);
        }
        money += ppl;
    }

    answer = QString("%1").arg(money);

    return answer;
}

int main()
{
    QString inputFilename = "C-small-attempt0.in", outputFilename = "C-small-attempt0.out";

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
            int r, k, n;
            fscanf(input, "%d %d %d", &r, &k, &n);

            QVector<int> groups;
            for(int i = 0; i < n; i++) {
                int gn;
                fscanf(input, "%d", &gn);

                groups.push_back(gn);
            }

            fprintf(output, "Case #%d: %s\n", c+1, solveCase(r, k, groups).toLatin1().data());
        }

        fclose(input);
        fclose(output);
    }

    return 0;
}
