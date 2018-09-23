class Ocd:
    def arrange(self, input):
        digits = list(map(int, list(input)))
        curIndex = len(digits)-1;
        while curIndex > 0:
            if self.shouldPad(digits, curIndex):
                digits = self.padMax(digits, curIndex)
                digits = self.decrIndex(digits, curIndex-1)
            curIndex -= 1
        return ''.join(map(str, digits)).lstrip('0')

    def shouldPad(self, digits, index):
        if digits[index-1] > digits[index]:
            return True;
        return False;

    def padMax(self, digits, fromIndex):
        for index in range(fromIndex, len(digits)):
            digits[index] = 9
        return digits

    def decrIndex(self, digits, index):
        digits[index] -= 1
        return digits