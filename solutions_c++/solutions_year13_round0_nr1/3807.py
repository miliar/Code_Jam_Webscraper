#include<cstdio>

int main() {
    int Z; scanf("%d ", &Z);
    int all = Z;
    while (Z--) {
        char T[5][5];
        for (int i=0; i<4; i++) {
            scanf("%s ", T[i]);
        }
        bool finished = true;
        int Ts = 0;
        int Os = 0;
        int Xs = 0;
        for (int i=0; i<4; i++) {
            Ts =0;
            Os = 0;
            Xs = 0;
            for (int j=0; j<4; j++) {
                if (T[i][j] == 'T') Ts++;
                if (T[i][j] == 'O') Os++;
                if (T[i][j] == 'X') Xs++;
                if (T[i][j] == '.') finished = false;
            }
            if ((Os >= 3) && (Ts + Os >= 4)) {
                printf("Case #%d: O won\n", all-Z);
                goto resolved;
            }
            if ((Xs >= 3) && (Ts + Xs >=4)) {
                printf("Case #%d: X won\n", all-Z);
                goto resolved;
            }
        }
        for (int i=0; i<4; i++) {
            Ts = 0;
            Os = 0;
            Xs = 0;
            for (int j=0; j<4; j++) {
                if (T[j][i] == 'T') Ts++;
                if (T[j][i] == 'O') Os++;
                if (T[j][i] == 'X') Xs++;
            }
            if ((Os >= 3) && (Ts + Os >= 4)) {
                printf("Case #%d: O won\n", all-Z);
                goto resolved;
            }
            if ((Xs >= 3) && (Ts + Xs >=4)) {
                printf("Case #%d: X won\n", all-Z);
                goto resolved;
            }
        }
        Ts = 0;
        Os = 0;
        Xs = 0;
        for (int i=0; i<4; i++) {
            if (T[i][i] == 'T') Ts++;
            if (T[i][i] == 'O') Os++;
            if (T[i][i] == 'X') Xs++;
            if ((Os >= 3) && (Ts + Os >= 4)) {
                printf("Case #%d: O won\n", all-Z);
                goto resolved;
            }
            if ((Xs >= 3) && (Ts + Xs >=4)) {
                printf("Case #%d: X won\n", all-Z);
                goto resolved;
            }
        }
        Ts = 0;
        Os = 0;
        Xs = 0;
        for (int i=0; i<4; i++) {
            if (T[i][3-i] == 'T') Ts++;
            if (T[i][3-i] == 'O') Os++;
            if (T[i][3-i] == 'X') Xs++;
            if ((Os >= 3) && (Ts + Os >= 4)) {
                printf("Case #%d: O won\n", all-Z);
                goto resolved;
            }
            if ((Xs >= 3) && (Ts + Xs >=4)) {
                printf("Case #%d: X won\n", all-Z);
                goto resolved;
            }
        }

        if (finished) {
            printf("Case #%d: Draw\n", all-Z);
        } else {
            printf ("Case #%d: Game has not completed\n", all-Z);
        }


resolved:
        int mama = 0;
    }
}
