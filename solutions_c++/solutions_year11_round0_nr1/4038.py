#include <cstdio>

using namespace std;

const int MAX_N = 100;

struct step {
    char c;
    int button;
};

int main () {
    int t, n;
    int sum, poso, posb, posbtn;
    step seq[MAX_N];
    bool find;

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        for (int j = 0; j < n; j++) {
            scanf(" %c %d", &seq[j].c, &seq[j].button);
        }

        sum = 0;
        poso = posb = 1;
        for (int j = 0; j < n; j++) {
            find = 0;
            if (seq[j].c == 'O') {
                for (int k = j+1; k < n; k++) {
                    if (seq[k].c == 'B') {
                        find = 1;
                        posbtn = seq[k].button;
                        break;
                    }
                }

                if (poso <= seq[j].button) {
                    while (poso < seq[j].button) {
                        poso++;
                        if (find) {
                            if (posb < posbtn) {
                                posb++;
                            } else if (posb > posbtn) {
                                posb--;
                            } else {
                                find = 0;
                            }
                        }
                        sum++;
                    }
                    if (find) {
                        if (posb < posbtn) {
                            posb++;
                        } else if (posb > posbtn) {
                            posb--;
                        }
                    }
                    sum++;
                } else {
                    while (poso > seq[j].button) {
                        poso--;
                        if (find) {
                            if (posb < posbtn) {
                                posb++;
                            } else if (posb > posbtn) {
                                posb--;
                            } else {
                                find = 0;
                            }
                        }
                        sum++;
                    }
                    if (find) {
                        if (posb < posbtn) {
                            posb++;
                        } else if (posb > posbtn) {
                            posb--;
                        }
                    }
                    sum++;
                }
            } else {
                for (int k = j+1; k < n; k++) {
                    if (seq[k].c == 'O') {
                        find = 1;
                        posbtn = seq[k].button;
                        break;
                    }
                }

                if (posb <= seq[j].button) {
                    while (posb < seq[j].button) {
                        posb++;
                        if (find) {
                            if (poso < posbtn) {
                                poso++;
                            } else if (poso > posbtn) {
                                poso--;
                            } else {
                                find = 0;
                            }
                        }
                        sum++;
                    }
                    if (find) {
                        if (poso < posbtn) {
                            poso++;
                        } else if (poso > posbtn) {
                            poso--;
                        }
                    }
                    sum++;
                } else {
                    while (posb > seq[j].button) {
                        posb--;
                        if (find) {
                            if (poso < posbtn) {
                                poso++;
                            } else if (poso > posbtn) {
                                poso--;
                            } else {
                                find = 0;
                            }
                        }
                        sum++;
                    }
                    if (find) {
                        if (poso < posbtn) {
                            poso++;
                        } else if (poso > posbtn) {
                            poso--;
                        }
                    }
                    sum++;
                }
            }
        }

        printf("Case #%d: %d\n", i, sum);
    }

    return 0;
}
