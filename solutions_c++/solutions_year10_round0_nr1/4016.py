//peterholak

#include <stdio.h>

int isOn(int device, int afterSnap) {
	if (!afterSnap)
		return false;
	int repeatedSize = (device==1?1:(2<<(device-2)));
	int prefix = 2*repeatedSize - 2;
	if (afterSnap < prefix)
		return false;
	int shiftedSnap = afterSnap - prefix - 1;
	int sector = shiftedSnap / repeatedSize;
	return !(sector & 1);
}

int main(int argc, char *argv[]) {
	int tasks;
	scanf("%d", &tasks);
	for (int t=0; t<tasks; t++) {
		int devices, snaps; //fuck one-letter variables
		scanf("%d %d", &devices, &snaps);
		bool allOn = true;
		for (int j=1; j<=devices; j++) {
			if (!isOn(j, snaps)) {
				allOn = false;
				break;
			}
		}
		printf("Case #%d: %s\n", t+1, allOn ? "ON" : "OFF");
	}
	return 0;
}
